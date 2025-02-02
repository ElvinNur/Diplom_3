import requests
from utils.config import MAIN_PAGE_URL

class UserCreationAPI:
    def __init__(self):
        self.base_url = MAIN_PAGE_URL
    
    def create_user(self, user_data):
        """Создаёт пользователя через API и возвращает JSON-ответ с accessToken."""
        url = f"{self.base_url}/api/auth/register"
        response = requests.post(url, json=user_data)
        if response.status_code != 200:
            raise Exception(f"Ошибка при создании пользователя: {response.status_code}, {response.text}")
        return response.json()

    def delete_user(self, access_token):
        """Удаляет пользователя по accessToken."""
        url = f"{self.base_url}/api/auth/user"
        headers = {"Authorization": f"{access_token}"}
        response = requests.delete(url, headers=headers)
        if response.status_code != 202:
            raise Exception(f"Ошибка при удалении пользователя: {response.status_code}, {response.text}")