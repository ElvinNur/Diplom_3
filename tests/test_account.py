import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.account_page import AccountPage

@allure.feature("Личный кабинет")
class TestAccount:

    @allure.title("Навигация по профилю в авторизованной зоне")  
    @allure.story("Тест функционала личного кабинета")
    def test_account_features(self, driver, created_user):
        user_data, access_token = created_user  # Получаем данные пользователя и токен из фикстуры

        with allure.step("Авторизация на сайте"):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login(user_data["email"], user_data["password"])  # Используем данные из фикстуры

        with allure.step("Переход в личный кабинет"):
            main_page = MainPage(driver)
            main_page.go_to_account()

        with allure.step("Проверяем, что страница профиля загружена"):
            account_page = AccountPage(driver)
            account_page.verify_profile_page_loaded()

        with allure.step("Переход в раздел 'История заказов'"):
            account_page.go_to_order_history()

        with allure.step("Выход из аккаунта"):
            account_page.logout()
