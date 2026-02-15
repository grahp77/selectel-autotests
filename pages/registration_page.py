from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

class RegistrationPage:
    """Страница регистрации my.selectel.ru/registration"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://my.selectel.ru/registration"
    
    def open(self):
        """Открыть страницу регистрации"""
        self.driver.get(self.url)
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
            print("✅ Страница загрузилась")
        except TimeoutException:
            print("⚠️ Страница загружалась долго, продолжаем...")
    
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url
    
    def take_screenshot(self, name):
        """Сделать скриншот"""
        timestamp = int(time.time())
        filename = f"screenshots/{name}_{timestamp}.png"
        self.driver.save_screenshot(filename)
        print(f"📸 Скриншот сохранен: {filename}")
        return filename
    
    def enter_email(self, email):
        """Ввести email"""
        try:
            field = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
            )
            field.clear()
            field.send_keys(email)
            entered_value = field.get_attribute("value")
            assert entered_value == email, f"Email ввелся неправильно: {entered_value}"
            print(f"✅ Email введен: {email}")
            return True
        except Exception as e:
            print(f"❌ Ошибка ввода email: {e}")
            self.take_screenshot("email_error")
            raise
    
    def enter_password(self, password):
        """Ввести пароль"""
        try:
            field = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
            )
            field.clear()
            field.send_keys(password)
            entered_value = field.get_attribute("value")
            assert len(entered_value) == len(password), "Пароль ввелся не полностью"
            print(f"✅ Пароль введен (длина: {len(password)})")
            return True
        except Exception as e:
            print(f"❌ Ошибка ввода пароля: {e}")
            self.take_screenshot("password_error")
            raise
    
    def click_generate_password(self):
        """Нажать кнопку генерации пароля"""
        try:
            button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Сгенерировать')]"))
            )
            button.click()
            print("✅ Кнопка генерации нажата")
            time.sleep(1)
            return True
        except:
            print("⚠️ Кнопка генерации не найдена")
            return False
    
    def click_newsletter_checkbox(self):
        """Кликнуть на чекбокс рассылки через input"""
        try:
            # Ищем input типа checkbox (он перекрывает span)
            checkbox_input = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox'].ant-checkbox-input"))
            )
            
            # Скроллим до элемента
            self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox_input)
            time.sleep(0.5)
            
            # Пробуем кликнуть через JavaScript (надежнее)
            self.driver.execute_script("arguments[0].click();", checkbox_input)
            print("✅ Чекбокс нажат через input")
            
            # Проверяем состояние по атрибуту checked
            is_checked = checkbox_input.get_attribute("checked") == "true" or checkbox_input.is_selected()
            print(f"Состояние чекбокса: {'выбран' if is_checked else 'не выбран'}")
            
            return is_checked
            
        except Exception as e:
            print(f"❌ Ошибка при клике на чекбокс: {e}")
            
            # Запасной вариант: клик по span
            try:
                checkbox_span = self.driver.find_element(By.CSS_SELECTOR, "span.ant-checkbox-inner")
                self.driver.execute_script("arguments[0].click();", checkbox_span)
                print("✅ Чекбокс нажат через span (запасной вариант)")
                time.sleep(0.5)
                
                # Пробуем определить состояние по родительскому классу
                parent = checkbox_span.find_element(By.XPATH, "..")
                parent_class = parent.get_attribute("class")
                is_checked = "ant-checkbox-checked" in parent_class
                print(f"Состояние чекбокса: {'выбран' if is_checked else 'не выбран'}")
                return is_checked
            except:
                return False
    
    def click_create_account(self):
        """Нажать кнопку создания аккаунта"""
        try:
            span = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Создать аккаунт')]"))
            )
            print(f"✅ Найден span с текстом: '{span.text}'")
            
            button = span.find_element(By.XPATH, "..")
            print(f"Родительский тег: {button.tag_name}")
            
            # Кликаем через JavaScript для надежности
            self.driver.execute_script("arguments[0].click();", button)
            print("✅ Кнопка создания аккаунта нажата через JavaScript")
            time.sleep(2)
            return True
        except Exception as e:
            print(f"❌ Ошибка при клике: {e}")
            self.take_screenshot("button_error")
            raise
    
    def get_password_value(self):
        """Получить значение поля пароля"""
        try:
            field = self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
            value = field.get_attribute("value")
            print(f"Значение поля пароля: {'*' * len(value) if value else 'пусто'}")
            return value
        except:
            return ""
    
    def is_email_field_displayed(self):
        """Проверить наличие поля email"""
        try:
            self.driver.find_element(By.CSS_SELECTOR, "input[type='email']")
            return True
        except:
            return False
    
    def is_password_field_displayed(self):
        """Проверить наличие поля пароля"""
        try:
            self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
            return True
        except:
            return False
    
    def is_create_account_button_displayed(self):
        """Проверить наличие кнопки создания аккаунта"""
        try:
            self.driver.find_element(By.XPATH, "//span[contains(text(), 'Создать аккаунт')]")
            return True
        except:
            return False