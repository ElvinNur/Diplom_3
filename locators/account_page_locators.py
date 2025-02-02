from selenium.webdriver.common.by import By

class AccountPageLocators:
    ORDER_HISTORY_BUTTON = (By.XPATH, '//a[text()="История заказов"]')
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')
    LAST_ORDER_IN_HISTORY = (By.XPATH, '(//li[contains(@class, "OrderHistory_listItem__2x95r")])[last()]//p')
    OPENED_MODAL = (By.XPATH, '//div[contains(@class, "modal_opened")]')