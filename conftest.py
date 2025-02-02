import pytest
import uuid
from utils.webdriver_factory import WebDriverFactory
from api.user_api import UserCreationAPI
from data import USER_TEMPLATE

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """Фикстура для создания WebDriver."""
    browser_type = request.param
    driver = WebDriverFactory.get_driver(browser_type)
    yield driver
    driver.quit()

@pytest.fixture
def user_api():
    """Фикстура для работы с API."""
    return UserCreationAPI()

@pytest.fixture
def created_user(user_api):
    """Фикстура для создания и удаления пользователя."""
    # Создаём уникального пользователя на основе шаблона
    user_data = USER_TEMPLATE.copy()
    user_data["email"] = f"test_{uuid.uuid4().hex}@example.com"  # Генерируем уникальный email

    user_response = user_api.create_user(user_data)
    assert "accessToken" in user_response, "Пользователь не был создан"

    access_token = user_response["accessToken"]

    yield user_data, access_token  # Передаём данные пользователя и токен в тест

    user_api.delete_user(access_token)  # Удаляем пользователя после теста