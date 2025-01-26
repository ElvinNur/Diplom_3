from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from .account_page import AccountPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()
    
    def go_to_account(self):
        """Переход в личный кабинет."""
        try:
            # Ожидание, пока кнопка станет кликабельной, и попытка клика
            account_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.ACCOUNT_BUTTON),
                "Кнопка 'Личный кабинет' не кликабельна."
            )
            account_button.click()
        except Exception as e:
            # Если клик не удался, выполняем наведение и клик через ActionChains
            account_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.locators.ACCOUNT_BUTTON),
                "Кнопка 'Личный кабинет' не найдена."
            )
            actions = ActionChains(self.driver)
            actions.move_to_element(account_button).perform()

            # Попытка клика через JavaScript после наведения
            self.driver.execute_script(
                "arguments[0].click();", account_button
            )
        return AccountPage(self.driver)