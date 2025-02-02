from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        
    def open_url(self, url):
        """Открывает указанный URL и ждет полной загрузки страницы."""
        self.driver.get(url)

    def find_element(self, locator):
        """Ищет элемент и возвращает его."""
        return self.driver.find_element(*locator)

    def get_current_url(self):
        """Возвращает текущий URL страницы."""
        return self.driver.current_url

    def is_correct_url(self, expected_url: str):
        """Проверяет, что текущий URL совпадает с ожидаемым."""
        return self.get_current_url() == expected_url

    def wait_and_click(self, locator):
        """Ожидание видимости элемента и клик по нему."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        """Ожидание элемента и ввод текста."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def wait_for_url(self, expected_url):
        """Ожидает, пока текущий URL страницы не станет ожидаемым."""
        self.wait.until(EC.url_to_be(expected_url))

    def wait_for_element_visibility(self, locator):
        """Ожидает, пока элемент станет видимым."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_invisibility(self, locator):
        """Ожидает, пока элемент станет невидимым."""
        self.wait.until(EC.invisibility_of_element_located(locator))

    def is_element_visible(self, locator):
        """Проверяет, что элемент видим на странице."""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element.is_displayed()
        except:
            return False

    def wait_for_element_presence(self, locator):
        """Ожидает, пока элемент появится в DOM."""
        return self.wait.until(EC.presence_of_element_located(locator))


    def js_click(self, locator, use_fallback=True):
        """
        Выполняет клик на элемент с помощью Selenium или JavaScript.

        :param locator: Локатор элемента (кортеж (By, "value")).
        :param use_fallback: Если True, выполняет наведение мыши и JS-клик, если стандартный клик не сработал.
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            if use_fallback:
                element = self.wait.until(EC.presence_of_element_located(locator))
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                self.driver.execute_script(
                    "if (arguments[0].click) { arguments[0].click(); } else { arguments[0].dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true })); }",
                    element
                )
            else:
                raise

    def wait_for_element_text_to_be(self, locator, expected_text, timeout=10):
        """
        Ожидает, пока текст элемента станет равным ожидаемому.

        :param locator: Локатор элемента (By, "value").
        :param expected_text: Ожидаемый текст элемента.
        :param timeout: Время ожидания в секундах.
        :return: True, если текст стал ожидаемым, иначе False.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                lambda d: d.find_element(*locator).text.strip() == expected_text
            )
        except TimeoutException:
            return False