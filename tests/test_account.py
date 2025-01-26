import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.account_page import AccountPage

@allure.feature("Личный кабинет")
class TestAccount:

    @allure.story("Тест функционала личного кабинета")
    def test_account_features(self, driver, unique_user, user_api):
        created_user = None
        try:
            with allure.step("Создание пользователя через API"):
                created_user = user_api.create_user(unique_user)
                assert "accessToken" in created_user, "Пользователь не был создан"

            with allure.step("Авторизация на сайте"):
                login_page = LoginPage(driver)
                login_page.open()
                login_page.login(unique_user["email"], unique_user["password"])

            with allure.step("Переход в личный кабинет"):
                main_page = MainPage(driver)
                account_page = main_page.go_to_account()

            with allure.step("Проверяем, что страница профиля загружена"):
                account_page.verify_profile_page_loaded()

            with allure.step("Переход в раздел 'История заказов'"):
                account_page.go_to_order_history()

            with allure.step("Выход из аккаунта"):
                account_page.logout()

        finally:
            with allure.step("Удаление пользователя через API"):
                if created_user:
                    user_api.delete_user(unique_user)