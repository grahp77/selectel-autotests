import pytest
from pages.main_page import MainPage

class TestMainPage:
    """Тесты для главной страницы selectel.ru"""
    
    def test_page_title(self, driver):
        """Проверка заголовка страницы"""
        main_page = MainPage(driver)
        main_page.open_main_page()
        title = main_page.get_page_title()
        assert "Selectel" in title, f"Заголовок '{title}' не содержит 'Selectel'"
    
    def test_logo_displayed(self, driver):
        """Проверка отображения логотипа"""
        main_page = MainPage(driver)
        main_page.open_main_page()
        assert main_page.is_logo_displayed(), "Логотип не отображается"
    
    def test_menu_items_present(self, driver):
        """Проверка наличия пунктов меню"""
        main_page = MainPage(driver)
        main_page.open_main_page()
        count = main_page.get_menu_items_count()
        assert count > 0, "Меню не содержит пунктов"
        print(f"Найдено пунктов меню: {count}")
    
    def test_footer_links_count(self, driver):
        """Проверка наличия ссылок в футере"""
        main_page = MainPage(driver)
        main_page.open_main_page()
        count = main_page.get_footer_links_count()
        assert count > 0, "В футере нет ссылок"
        print(f"Найдено ссылок в футере: {count}")
    
    def test_login_button_clickable(self, driver):
        """Проверка кликабельности кнопки 'Войти'"""
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_login_button()
        current_url = driver.current_url
        assert "login" in current_url or "auth" in current_url, \
            f"Не удалось перейти на страницу логина. Текущий URL: {current_url}"