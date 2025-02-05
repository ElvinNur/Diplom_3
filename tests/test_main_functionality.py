import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.modal_ingredient_page import ModalWindowPage
from pages.modal_order_page import ModalOrderPage
from utils.config import FEED_PAGE_URL, MAIN_PAGE_URL

@allure.feature("Основной функционал")
class TestCoreFeatures:

    @allure.title("Авторизация, навигация по сайту и проверка ключевых элементов")  
    @allure.story("Проверка основного функционала")
    def test_navigation_and_main_elements(self, driver, created_user):
        """
        Проверяет авторизацию, переходы между страницами, открытие модальных окон и оформление заказа.
        """
        user_data, access_token = created_user  # Получаем данные пользователя и токен из фикстуры

        with allure.step("Авторизация на сайте"):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login(user_data["email"], user_data["password"])

        with allure.step("Переход на 'Лента заказов'"):
            main_page = MainPage(driver)
            main_page.go_to_feed()
            assert main_page.get_current_url() == FEED_PAGE_URL, "Не удалось перейти на страницу 'Лента заказов'"
            feed_page = OrderFeedPage(driver)
            assert feed_page.is_feed_title_visible(), "Заголовок 'Лента заказов' отсутствует"

        with allure.step("Переход на 'Конструктор'"):
            main_page.go_to_constructor()
            assert main_page.is_constructor_title_visible(), "Текст 'Соберите бургер' отсутствует"
            assert main_page.get_current_url().rstrip('/') == MAIN_PAGE_URL.rstrip('/'), "Не удалось перейти на страницу 'Конструктор'"

        with allure.step("Открытие модального окна"):
            main_page.click_on_ingredient()
            modal_page = ModalWindowPage(driver)
            assert modal_page.is_modal_visible(), "Модальное окно не появилось"

        with allure.step("Закрытие модального окна"):
            modal_page.close_modal()
            assert not modal_page.is_modal_visible(), "Модальное окно не закрылось"

        with allure.step("Смена каунтера при выборе ингредиента"):    
            main_page.drag_ingredient_to_cart()
            assert main_page.is_counter_change(), "Каунтер не изменился"

        with allure.step("Оформление заказа"):
            main_page.drag_ingredient_to_cart()
            main_page.click_on_order()
            modal_page = ModalOrderPage(driver)
            assert modal_page.is_order_modal_visible(), "Окно заказа не появилось"
