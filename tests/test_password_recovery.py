import pytest
import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from api.user_api import UserCreationAPI


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Проверка восстановления пароля пользователя") 
    @allure.story("Тест восстановления пароля")
    def test_password_recovery(self, driver, created_user):
        user_data, access_token = created_user  # Получаем данные пользователя и токен из фикстуры

        with allure.step("Авторизация на сайте"):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login(user_data["email"], user_data["password"])  # Используем данные из фикстуры


        with allure.step("Открываем страницу логина"):
            login_page = LoginPage(driver)
            login_page.open()

        with allure.step("Переходим на страницу восстановления пароля"):
            login_page.click_forgot_password_link()

        with allure.step("Вводим email и отправляем запрос на восстановление"):
            forgot_password_page = ForgotPasswordPage(driver)
            forgot_password_page.enter_email(user_data["email"])
            forgot_password_page.click_recover_button()

        with allure.step("Проверяем загрузку страницы сброса пароля"):
            reset_password_page = ResetPasswordPage(driver)
            reset_password_page.verify_reset_password_page_loaded()

        with allure.step("Проверяем активацию поля пароля"):
            reset_password_page.toggle_password_visibility()
            reset_password_page.verify_password_field_active()
