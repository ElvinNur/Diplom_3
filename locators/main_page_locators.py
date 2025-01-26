from selenium.webdriver.common.by import By

class MainPageLocators:
    # ACCdOUNT_BUTTON = (By.XPATH, '//a[contains(@class, "AppHeader_header__link__3D_hX") and .//p[text()="Личный Кабинет"]]')
    # ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'a.AppHeader_header__link__3D_hX > p.AppHeader_header__linkText__3q_va')
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, "#root > div > header > nav > a")