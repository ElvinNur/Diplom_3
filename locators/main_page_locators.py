from selenium.webdriver.common.by import By

class MainPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, '//a[contains(@class, "AppHeader") and .//p[text()="Личный Кабинет"]]')
    FEED_BUTTON = (By.XPATH, '//a[contains(@class, "AppHeader") and .//p[text()="Лента Заказов"]]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//a[contains(@class, "AppHeader") and .//p[text()="Конструктор"]]')
    CONSTRUCTOR_TITLE = (By.XPATH, '//h1[text()="Соберите бургер"]')
    FIRST_INGREDIENT = (By.XPATH, '//a[contains(@class, "BurgerIngredient") and .//p[text()="Флюоресцентная булка R2-D3"]]')
    CART = (By.XPATH,'//span[@class="constructor-element__row"]')
    COUNTER = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d" and .//p[text() = "2"]]')
    ORDER_BUTTON = (By.XPATH, '//button[text() = "Оформить заказ"]')