from .base_page import BasePage
from locators.modal_window_locators import ModalWindowLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ModalWindowPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ModalWindowLocators()
   
    def is_modal_visible(self):
        """Проверяет, что модальное окно отображается."""
        try:
            self.wait_for_element_visibility(self.locators.MODAL_OPEN)
            return True  # Модальное окно видно
        
        except TimeoutException:
            return False  # Модальное окно не видно


    def close_modal(self):
        """Закрывает модальное окно."""
        self.js_click(self.locators.CLOSE_BUTTON)