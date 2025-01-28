from selenium.webdriver.common.by import By

class ModalWindowLocators:
    MODAL_OPEN = (By.XPATH, '//section[contains(@class, "modal_opened")]')
    CLOSE_BUTTON = (By.XPATH, '//section[contains(@class, "modal_opened")]//button[contains(@class, "close")]') 