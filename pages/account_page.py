from .base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import LOGIN_PAGE_URL, PROFILE_PAGE_URL, ORDER_HISTORY_PAGE_URL

 
class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AccountPageLocators()

    def verify_profile_page_loaded(self):
        """Проверяем, что страница профиля загружена."""
        self.wait_for_url(PROFILE_PAGE_URL)
        
        assert self.is_correct_url(PROFILE_PAGE_URL), "Не удалось загрузить страницу профиля"
            
    def go_to_order_history(self):
        """Переход в раздел 'История заказов'."""
        self.js_click(self.locators.ORDER_HISTORY_BUTTON)
        self.wait_for_url(ORDER_HISTORY_PAGE_URL)
        
        assert self.is_correct_url(ORDER_HISTORY_PAGE_URL), "Не удалось загрузить страницу 'История заказов'"

            
    def get_last_order_number(self):
        """
        Получает номер последнего заказа из истории заказов.
        :return: номер заказа в формате строки.
        """
        # Ожидаем появления последнего заказа в истории
        last_order_element = self.wait_for_element_visibility(self.locators.LAST_ORDER_IN_HISTORY)

        return last_order_element.text

    def logout(self):
        """Выход из аккаунта."""
        self.js_click(self.locators.LOGOUT_BUTTON)
        self.wait_for_url(LOGIN_PAGE_URL)

        assert self.is_correct_url(LOGIN_PAGE_URL), "Не удалось выйти из аккаунта"
    