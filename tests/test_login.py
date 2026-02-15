import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

class TestLogin:
    """Тесты для проверки входа на сайт"""
    
    def test_login_button_opens_new_tab(self, driver):
        """Тест: при клике на 'Войти' открывается новая вкладка со страницей входа"""
        
        # Шаг 1: Открываем главную страницу
        main_page = MainPage(driver)
        main_page.open()
        
        # Запоминаем текущую вкладку
        original_window = driver.current_window_handle
        
        # Шаг 2: Нажимаем кнопку "Войти"
        main_page.click_login_button()
        
        # Шаг 3: Ждем появления новой вкладки (максимум 10 секунд)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.number_of_windows_to_be(2))
        
        # Шаг 4: Переключаемся на новую вкладку
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        
        # Шаг 5: Проверяем URL новой вкладки
        current_url = driver.current_url
        assert "login" in current_url, f"Не удалось перейти на страницу логина. URL: {current_url}"
        
        # Шаг 6: Возвращаемся на исходную вкладку
        driver.switch_to.window(original_window)
        assert driver.current_url == "https://selectel.ru/", "Не вернулись на главную страницу"
