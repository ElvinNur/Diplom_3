import pytest
import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from api.user_api import UserCreationAPI

@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.story("Тест восстановления пароля")
    def test_password_recovery(self, driver, unique_user, user_api):
        created_user = None
        try:
            with allure.step("Создание пользователя через API"):
                created_user = user_api.create_user(unique_user)
                assert "accessToken" in created_user, "Пользователь не был создан"

            with allure.step("Открываем страницу логина"):
                login_page = LoginPage(driver)
                login_page.open()

            with allure.step("Переходим на страницу восстановления пароля"):
                forgot_password_page = login_page.click_forgot_password_link()

            with allure.step("Вводим email и отправляем запрос на восстановление"):
                forgot_password_page.enter_email(unique_user["email"])
                forgot_password_page.click_recover_button()

            with allure.step("Проверяем загрузку страницы сброса пароля"):
                reset_password_page = ResetPasswordPage(driver)
                reset_password_page.verify_reset_password_page_loaded()

            with allure.step("Проверяем активацию поля пароля"):
                reset_password_page.toggle_password_visibility()
                reset_password_page.verify_password_field_active()

        finally:
            with allure.step("Удаление пользователя через API"):
                if created_user:
                    user_api.delete_user(unique_user)