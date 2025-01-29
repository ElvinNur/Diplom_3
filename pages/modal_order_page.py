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
        """Проверяет, что модальное окно Заказа отображается."""
        try:
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located(self.locators.ORDER_MODAL_OPEN)
            )
            return True  # Модальное окно видно
        except TimeoutException:
            return False  # Модальное окно не видно
        
    def get_order_number(self):
        # Ждем, пока появится элемент, сигнализирующий о готовности номера заказа
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.locators.CONFIRMATION_ELEMENT))
        """Получает номер заказа из модального окна."""
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators.ORDER_NUMBER)).text
    
    def close_modal(self):
        """Закрывает модальное окно."""
        self.js_click(self.locators.CLOSE_BUTTON)