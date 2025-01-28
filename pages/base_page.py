from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

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
        try:
            # Ожидание присутствия элемента в DOM
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            # Проверка, что элемент видим
            return element.is_displayed()
        except:
            # Если элемент не найден или невидим, возвращаем False
            return False
        
        
    def js_click(self, locator, use_fallback=True):
        """
        Выполняет клик на элемент с помощью Selenium или JavaScript.

        :param locator: Локатор элемента (кортеж типа (By, "value")).
        :param use_fallback: Если True, выполняет наведение мыши и JS-клик, если стандартный клик не сработал.
        """
        try:
            # Ожидание, пока элемент станет кликабельным, и попытка стандартного клика
            element = WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable(locator),
                f"Элемент с локатором {locator} не кликабелен."
            )
            element.click()
        except Exception as e:
            if use_fallback:
                # Если стандартный клик не удался, выполняем наведение мыши и клик через JS
                element = WebDriverWait(self.driver, 1).until(
                    EC.presence_of_element_located(locator),
                    f"Элемент с локатором {locator} не найден."
                )
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()

                # Попытка клика через JavaScript после наведения
                self.driver.execute_script(
                    "if (arguments[0].click) { arguments[0].click(); } else { arguments[0].dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true })); }",
                    element
                )
            else:
                raise
        