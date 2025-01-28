import pytest
from utils.webdriver_factory import WebDriverFactory
from api.user_api import UserCreationAPI


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """Фикстура для создания WebDriver."""
    browser_type = request.param
    driver = WebDriverFactory.get_driver(browser_type)
    yield driver
    driver.quit()

@pytest.fixture
def unique_user():
    """Фикстура для создания уникального пользователя."""
    return {
        "email": "unique1234_user_zxcqwe@example.com",
        "password": "securepassword",
        "name": "TestUser"
    }

@pytest.fixture
def user_api():
    """Фикстура для работы с API."""
    return UserCreationAPI()
