import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

class TestLogin:
    """Тесты для проверки входа на сайт"""
    
    def test_login_button_opens_new_tab(self, driver):
        """Тест: при клике на 'Войти' открывается новая вкладка со страницей входа"""
        
        main_page = MainPage(driver)
        main_page.open()
        
        original_window = driver.current_window_handle
        
        main_page.click_login_button()
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.number_of_windows_to_be(2))
        
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        
        current_url = driver.current_url
        assert "login" in current_url, f"Не удалось перейти на страницу логина. URL: {current_url}"
        
        driver.switch_to.window(original_window)
        assert driver.current_url == "https://selectel.ru/", "Не вернулись на главную страницу"
