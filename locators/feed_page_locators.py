from selenium.webdriver.common.by import By

class FeedPageLocators:
    FEED_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')
    FIRST_ORDER = (By.XPATH, '//a[contains(@class, "OrderHistory")]')
    ORDER_COUNTER_TOTAL = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    ORDER_COUNTER_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    READY_ORDER = (By.XPATH, '//ul[contains(@class, "orderListReady")]/li')
    FIRST_ORDER_IN_FEED = (By.XPATH, '(//li[contains(@class, "OrderHistory_listItem__2x95r")])[1]//p')