from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    """Базовый класс для всех Page Object"""
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self, url: str):
        """Открыть страницу"""
        self.driver.get(url)
    
    def find_element(self, locator: tuple):
        """Найти элемент с ожиданием"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click(self, locator: tuple):
        """Кликнуть на элемент"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys(self, locator: tuple, text: str):
        """Ввести текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_title(self) -> str:
        """Получить заголовок страницы"""
        return self.driver.title
    
    def take_screenshot(self, name: str):
        """Сделать скриншот (полезно при падении тестов)"""
        self.driver.save_screenshot(f"screenshots/{name}.png")