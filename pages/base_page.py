from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def get_current_url(self):
        """Возвращает текущий URL страницы."""
        return self.driver.current_url

    def is_correct_url(self, expected_url: str):
        """Проверяет, что текущий URL совпадает с ожидаемым."""
        return self.get_current_url() == expected_url

    def wait_and_click(self, locator, timeout=10):
        """Ожидание видимости элемента и клик по нему."""
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text, timeout=10):
        """Ожидание элемента и ввод текста."""
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    
    def is_element_visible(self, locator, timeout=10):
        """Проверяет, что элемент видим на странице."""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def js_click(self, locator):
        """Выполняет клик на элемент с помощью JavaScript."""
        element = self.driver.find_element(*locator)
        self.driver.execute_script("if (arguments[0].click) { arguments[0].click(); } else { arguments[0].dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true })); }", element)
        