from .base_page import BasePage
from locators.modal_order_locators import ModalOrderLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ModalOrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ModalOrderLocators()
   
    def is_order_modal_visible(self):
        """Проверяет, что модальное окно отображается."""
        try:
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located(self.locators.ORDER_MODAL_OPEN)
            )
            return True  # Модальное окно видно
        except TimeoutException:
            return False  # Модальное окно не видно