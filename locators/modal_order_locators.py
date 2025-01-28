from selenium.webdriver.common.by import By

class ModalOrderLocators:
    ORDER_MODAL_OPEN = (By.XPATH, '//section[contains(@class, "modal_opened")]')
    