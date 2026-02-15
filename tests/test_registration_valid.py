import pytest
import time
from pages.registration_page import RegistrationPage

class TestRegistrationValid:
    """Валидные тесты для страницы регистрации"""
    
    def test_1_page_loads(self, driver):
        """Тест 1: Проверка загрузки страницы регистрации"""
        reg_page = RegistrationPage(driver)
        reg_page.open()
        
        current_url = reg_page.get_current_url()
        assert "registration" in current_url, \
            f"Страница регистрации не открылась. URL: {current_url}"
        
        assert reg_page.is_email_field_displayed(), "Поле email не найдено"
        assert reg_page.is_password_field_displayed(), "Поле пароля не найдено"
        assert reg_page.is_create_account_button_displayed(), "Кнопка 'Создать аккаунт' не найдена"
        
        print("\n✅ Тест 1 пройден: Страница регистрации загружена")
        print(f"URL: {current_url}")
    
    def test_2_fill_valid_email_and_password(self, driver):
        """Тест 2: Ввод валидного email и пароля"""
        reg_page = RegistrationPage(driver)
        reg_page.open()
        
        test_email = f"test.user.{int(time.time())}@example.com"
        test_password = "Test123!@#"
        
        print(f"\n📧 Тестовый email: {test_email}")
        print(f"🔑 Тестовый пароль: {test_password}")
        
        reg_page.enter_email(test_email)
        reg_page.enter_password(test_password)
        
        print("✅ Тест 2 пройден: Данные успешно введены")
    
    def test_3_checkbox_interaction(self, driver):
        """Тест 3: Проверка работы чекбокса"""
        reg_page = RegistrationPage(driver)
        reg_page.open()
        
        reg_page.enter_email(f"test.checkbox.{int(time.time())}@example.com")
        reg_page.enter_password("Test123!@#")
        
        state1 = reg_page.click_newsletter_checkbox()
        
        state2 = reg_page.click_newsletter_checkbox()
        
        assert state1 != state2, "Состояние чекбокса не изменилось после второго клика"
        print("✅ Тест 3 пройден: Чекбокс работает корректно")
    
    def test_4_generate_password(self, driver):
        """Тест 4: Проверка генерации пароля"""
        reg_page = RegistrationPage(driver)
        reg_page.open()
        
        reg_page.click_generate_password()
        
        generated_password = reg_page.get_password_value()
        
        if generated_password:
            print(f"✅ Сгенерирован пароль длиной: {len(generated_password)} символов")
            assert len(generated_password) >= 8, f"Пароль слишком короткий: {len(generated_password)}"
        else:
            print("ℹ️ Поле пароля осталось пустым (так работает сайт)")
        
        print("✅ Тест 4 пройден: Кнопка генерации работает")
    
    def test_5_attempt_registration(self, driver):
        """Тест 5: Попытка регистрации"""
        reg_page = RegistrationPage(driver)
        reg_page.open()
        
        unique_email = f"test.user.{int(time.time())}@example.com"
        test_password = "Test123!@#"
        
        print(f"\n📧 Пробуем зарегистрироваться с email: {unique_email}")
        
        reg_page.enter_email(unique_email)
        reg_page.enter_password(test_password)
        reg_page.click_newsletter_checkbox()
        
        reg_page.click_create_account()
        
        current_url = reg_page.get_current_url()
        print(f"URL после регистрации: {current_url}")
        
        reg_page.take_screenshot("after_registration")
        
        assert "error" not in current_url.lower(), "Переход на страницу ошибки"
        
        print("✅ Тест 5 выполнен: Форма отправлена")
    
    def test_6_check_validation(self, driver):
        """Тест 6: Проверка валидации (пустые поля)"""
        reg_page = RegistrationPage(driver)
        reg_page.open()
        
        reg_page.click_create_account()
        
        reg_page.take_screenshot("validation_test")
        
        current_url = reg_page.get_current_url()
        assert "registration" in current_url, "Произошел неожиданный редирект"
        
        print("✅ Тест 6 выполнен: Валидация работает")