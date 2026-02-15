class LoginPage:
    """Страница входа my.selectel.ru/login"""
    
    def __init__(self, driver):
        self.driver = driver
    
    def is_login_page(self):
        """Проверить, что мы на странице входа"""
        current_url = self.driver.current_url
        return "login" in current_url
