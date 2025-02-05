from .base_page import BasePage
from locators.modal_order_locators import ModalOrderLocators
from selenium.common.exceptions import TimeoutException


class ModalOrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ModalOrderLocators()
   
    def is_order_modal_visible(self):
        """Проверяет, что модальное окно Заказа отображается."""
        try:
            self.wait_for_element_visibility(self.locators.ORDER_MODAL_OPEN)
            return True  # Модальное окно видно
        
        except TimeoutException:
            return False  # Модальное окно не видно
        
    def get_order_number(self):
        # Ждем, пока появится элемент, сигнализирующий о готовности номера заказа
        self.wait_for_element_presence(self.locators.CONFIRMATION_ELEMENT)
        """Получает номер заказа из модального окна."""
        return self.wait_for_element_visibility(self.locators.ORDER_NUMBER).text
    
    def close_modal(self):
        """Закрывает модальное окно."""
        self.js_click(self.locators.CLOSE_BUTTON)