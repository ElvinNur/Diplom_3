from .base_page import BasePage
from locators.feed_page_locators import FeedPageLocators

class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = FeedPageLocators()

    def is_feed_title_visible(self):
        """Проверяет наличие заголовка 'Лента заказов'."""
        return self.is_element_visible(self.locators.FEED_TITLE)