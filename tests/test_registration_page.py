import pytest
from pages.registration_page import RegistrationPage

class TestRegistrationPage:
    """Тесты для страницы регистрации (из Задания 1)"""
    
    def test_registration_page_loads(self, driver):
        """Проверка загрузки страницы регистрации"""
        reg_page = RegistrationPage(driver)
        reg_page.open_registration_page()
        assert "registration" in reg_page.get_current_url(), \
            "Страница регистрации не открылась"
    
    def test_email_field_validation_cyrillic(self, driver):
        """Тест BUG-006: Проверка обработки кириллицы в email"""
        reg_page = RegistrationPage(driver)
        reg_page.open_registration_page()
        
        reg_page.enter_email("test@gmail.ком")
        reg_page.enter_password("Test12345!")
        reg_page.click_create_account()
        
        assert "registration" in reg_page.get_current_url(), \
            "Страница перезагрузилась или произошел редирект"
        
        assert reg_page.is_error_message_displayed(), \
            "Нет сообщения об ошибке при вводе некорректного email"
    
    def test_long_email_validation(self, driver):
        """Тест BUG-007: Проверка обработки слишком длинного email"""
        reg_page = RegistrationPage(driver)
        reg_page.open_registration_page()
        
        long_local = "a" * 150
        long_domain = "b" * 150
        long_email = f"{long_local}@{long_domain}.com"
        
        reg_page.enter_email(long_email)
        reg_page.enter_password("Test12345!")
        reg_page.click_create_account()
        
        assert "registration" in reg_page.get_current_url(), \
            "Возможно, произошла ошибка сервера (редирект или краш)"
    
    def test_duplicate_registration(self, driver):
        """Тест BUG-008: Проверка повторной регистрации существующего email"""
        reg_page = RegistrationPage(driver)
        reg_page.open_registration_page()
        
        test_email = "test@selectel.ru"
        
        reg_page.enter_email(test_email)
        reg_page.enter_password("NewPass123!")
        reg_page.click_create_account()
        
        current_url = reg_page.get_current_url()
        assert "registration" in current_url, \
            f"Произошел редирект при повторной регистрации. URL: {current_url}"
        
        assert reg_page.is_error_message_displayed(), \
            "Нет сообщения о том, что email уже зарегистрирован"
    
    def test_support_link_mailto(self, driver):
        """Тест BUG-009: Проверка ссылки на поддержку"""
        reg_page = RegistrationPage(driver)
        reg_page.open_registration_page()
        
        support_element = driver.find_element(*reg_page.SUPPORT_LINK)
        href = support_element.get_attribute("href")
        
        assert href.startswith("mailto:"), \
            f"Ссылка поддержки не является mailto: {href}"
        assert "support@selectel.ru" in href, \
            "Email поддержки не соответствует ожидаемому"
    
    def test_generate_password_button(self, driver):
        """Тест BUG-003: Проверка кнопки генерации пароля"""
        reg_page = RegistrationPage(driver)
        reg_page.open_registration_page()
        
        reg_page.click_generate_password()
        
        password_field = driver.find_element(*reg_page.PASSWORD_FIELD)
        generated_password = password_field.get_attribute("value")
        
        assert generated_password, "Пароль не был сгенерирован (поле пустое)"
        assert len(generated_password) >= 8, \
            f"Сгенерированный пароль слишком короткий: {len(generated_password)} символов"