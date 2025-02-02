import pytest
import allure
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from pages.modal_ingredient_page import ModalWindowPage
from pages.main_page import MainPage
from pages.account_page import AccountPage
from pages.modal_order_page import ModalOrderPage

@allure.feature("Лента заказов")
class TestOrderFeed:
    
    @allure.title("Полное флоу оформления заказа и его отображение")  
    @allure.story("Проверка Ленты заказов")
    def test_order_feed(self, driver, created_user):
        user_data, access_token = created_user  # Получаем данные пользователя и токен из фикстуры

        with allure.step("Авторизация на сайте"):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login(user_data["email"], user_data["password"])
            
        with allure.step("Переход в 'Ленту заказов'"):
            main_page = MainPage(driver)
            main_page.button_order_is_visible()
            feed_page = OrderFeedPage(driver)
            feed_page.open_order_feed()

        with allure.step("Проверка открытия деталей заказа"):
            feed_page.open_order_details()
            modal_page = ModalWindowPage(driver)
            assert modal_page.is_modal_visible(), "Модальное окно не появилось"
            modal_page.close_modal()

        with allure.step("Запоминание текущего количества выполненных заказов"):
            completed_total_before = feed_page.get_completed_orders_total()
            completed_today_before = feed_page.get_completed_orders_today()

        with allure.step("Создание нового заказа"):
            main_page.go_to_main()
            main_page.place_order()
            modal = ModalOrderPage(driver)
            order_number = modal.get_order_number()
            assert order_number, "Заказ не оформился"

        with allure.step("Закрытие модального окна"):
            modal.close_modal()
            assert not modal.is_order_modal_visible(), "Модальное окно не закрылось"

        with allure.step("Проверка увеличения счетчиков заказов"):
            feed_page.open_order_feed()
            completed_total_after = feed_page.get_completed_orders_total()
            completed_today_after = feed_page.get_completed_orders_today()
            assert completed_total_after > completed_total_before, "Счётчик 'Выполнено за всё время' не изменился"
            assert completed_today_after > completed_today_before, "Счётчик 'Выполнено за сегодня' не изменился"

        with allure.step("Проверка, что заказ появился в 'В работе'"):
            assert feed_page.wait_for_element_text_to_change(order_number), \
                f"Ожидали 0{order_number}, но не нашли в списке заказов"

        with allure.step("Проверка наличия заказа в 'Истории заказов'"):
            first_order_number = feed_page.get_first_order_number()

        with allure.step("Переход в личный кабинет"):
            main_page.go_to_account()
            account_page = AccountPage(driver)
            account_page.go_to_order_history()
            assert first_order_number == account_page.get_last_order_number(), \
                f"Номер заказа в истории не совпадает: ожидали {first_order_number}, получили {account_page.get_last_order_number()}"
