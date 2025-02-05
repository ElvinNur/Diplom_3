from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.common.exceptions import TimeoutException
from utils.config import MAIN_PAGE_URL

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()
    
    def go_to_account(self):
        """Переход в личный кабинет."""
        self.js_click(self.locators.ACCOUNT_BUTTON)
    
    def go_to_feed(self):
        """Переход на 'Лента заказов'."""
        self.js_click(self.locators.FEED_BUTTON)
        
    def go_to_main(self):
        """Переход на главную."""
        self.js_click(self.locators.STELLAR_BURGERS)

    def go_to_constructor(self):
        """Переход на 'Конструктор'."""
        self.js_click(self.locators.CONSTRUCTOR_BUTTON)
        
    def button_order_is_visible(self):
        """Проверяет наличие заголовка 'Соберите бургер'."""
        return self.is_element_visible(self.locators.ORDER_BUTTON)

    def is_constructor_title_visible(self):
        """Проверяет наличие заголовка 'Соберите бургер'."""
        return self.is_element_visible(self.locators.CONSTRUCTOR_TITLE)

    def click_on_ingredient(self):
        """Клик на ингредиент."""
        self.js_click(self.locators.FIRST_INGREDIENT)
        
    def click_on_order(self):
        """Клик на Оформить заказ."""
        self.js_click(self.locators.ORDER_BUTTON)
        
    def is_counter_change(self):
        """Проверяет, что каунтер изменился."""
        try:
            self.is_element_visible(self.locators.COUNTER)
            return True  # Каунтер сменился на 2
        
        except TimeoutException:
            return False  # Каунтер не изменился 
        
    def drag_ingredient_to_cart(self):    
        """Перетаскивает ингредиент в корзину с использованием JavaScript."""
        ingredient = self.find_element(self.locators.FIRST_INGREDIENT)
        cart = self.find_element(self.locators.CART)
        self.drag_and_drop_js(ingredient, cart)
        
    def place_order(self):
        """Добавляет три ингредиента в корзину и оформляет заказ."""
        
        def drag_and_drop(ingredient_locator, cart_locator):
            """Перетаскивает ингредиент в корзину через JavaScript."""
            ingredient = self.find_element(ingredient_locator)
            cart = self.find_element(cart_locator)
            self.drag_and_drop_js(ingredient, cart)

        # Перетаскиваем первый ингредиент (булку)
        drag_and_drop(self.locators.FIRST_INGREDIENT, self.locators.CART)

        # Кликаем на вкладку "Соусы"
        self.js_click(self.locators.SAUCES_BUTTON)

        # Перетаскиваем второй ингредиент (соус)
        drag_and_drop(self.locators.SECOND_INGREDIENT, self.locators.CART)

        # Кликаем на вкладку "Начинки"
        self.js_click(self.locators.FILLINGS_BUTTON)

        # Перетаскиваем третий ингредиент (начинку)
        drag_and_drop(self.locators.THIRD_INGREDIENT, self.locators.CART)

        # Нажимаем "Оформить заказ"
        self.js_click(self.locators.ORDER_BUTTON)