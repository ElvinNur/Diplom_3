from .base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
from utils.config import FEED_PAGE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = FeedPageLocators()

    def is_feed_title_visible(self):
        """Проверяет наличие заголовка 'Лента заказов'."""
        return self.is_element_visible(self.locators.FEED_TITLE)
    
    def open_order_feed(self):
        """Переходим на страницу Лента Заказов."""
        self.driver.get(FEED_PAGE_URL)
        
    def open_order_details(self):
        """Клик на последний заказ."""
        self.js_click(self.locators.FIRST_ORDER)
        
    def get_completed_orders_total(self):
        """Возвращает значение счётчика 'Выполнено за всё время'."""
        return int(WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.locators.ORDER_COUNTER_TOTAL)).text)

    def get_completed_orders_today(self):
        """Возвращает значение счётчика 'Выполнено за сегодня'."""
        return int(WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self.locators.ORDER_COUNTER_TODAY)).text)
    
    def wait_for_element_text_to_change(self, expected_number, timeout=10):
        """
        Ожидает, пока текст элемента изменится на "0{expected_number}".
        
        :param expected_number: Число, которое должно появиться с префиксом '0'.
        :param timeout: Время ожидания в секундах.
        :return: True, если текст изменился, иначе False.
        """
        expected_text = f"0{expected_number}"

        try:
            return WebDriverWait(self.driver, timeout).until(
                lambda d: d.find_element(*self.locators.READY_ORDER).text.strip() == expected_text
            )
        except TimeoutException:
            return False
    
    def get_order_in_progress(self):
        """Возвращает номер заказа без ведущих нулей."""
        order_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.READY_ORDER)
        ).text.strip()
        
        return order_text.lstrip("0")
    
    def get_first_order_number(self):
        """
        Получает номер первого заказа из ленты заказов.
        :return: номер заказа в формате строки.
        """
        # Ожидаем появления последнего заказа в истории
        first_order_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.FIRST_ORDER_IN_FEED),
            "Последний заказ не найден в истории заказов"
        )

        return first_order_element.text