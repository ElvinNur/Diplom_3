from selenium.webdriver.common.by import By

class ModalOrderLocators:
    ORDER_MODAL_OPEN = (By.XPATH, '//section[contains(@class, "modal_opened")]')
    ORDER_NUMBER = (By.XPATH, '//section[contains(@class, "modal_opened")]//h2')
    CLOSE_BUTTON = (By.XPATH, '//section[contains(@class, "modal_opened")]//button[contains(@class, "close")]') 
    CONFIRMATION_ELEMENT = (By.XPATH, '//div[@class="Modal_modal__P3_V5"]') 