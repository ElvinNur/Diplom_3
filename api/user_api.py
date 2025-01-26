import requests
from utils.config import BASE_URL

class UserCreationAPI:
    def __init__(self):
        self.base_url = BASE_URL

    def create_user(self, unique_user):
        """Создаёт пользователя через API. Возвращает JSON-ответ."""
        url = f"{self.base_url}/api/auth/register"
        resp = requests.post(url, json=unique_user)
        if resp.status_code != 200:
            raise Exception(f"Ошибка при создании пользователя: {resp.status_code}, {resp.text}")
        return resp.json()

    def delete_user(self, unique_user):
        """Удаляет пользователя по accessToken. Возвращает статус-код."""
        # Авторизация пользователя
        login_url = f"{self.base_url}/api/auth/login"
        login_response = requests.post(login_url, json=unique_user)
        if login_response.status_code != 200:
            raise Exception(f"Ошибка при авторизации: {login_response.status_code}, {login_response.text}")

        # Получение токена
        token = login_response.json().get("accessToken")
        if not token:
            raise Exception("Не удалось получить accessToken")

        # Удаление пользователя
        delete_url = f"{self.base_url}/api/auth/user"
        headers = {"Authorization": f"{token}"}
        resp = requests.delete(delete_url, headers=headers)
        if resp.status_code != 202:
            raise Exception(f"Ошибка при удалении пользователя: {resp.status_code}, {resp.text}")
        return resp.status_code