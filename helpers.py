"""
Модуль с процедурными функциями-хелперами для работы с API курьеров.
Необъодимо перенести эту логику в класс CourierAPIClient в api_client.py.
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:5001/api")
AUTH_TOKEN = os.getenv("AUTH_TOKEN", "test_token_123")


def _get_auth_header():
    """Возвращает заголовок авторизации."""
    if not AUTH_TOKEN:
        raise ValueError("AUTH_TOKEN не задан")
    return {"Authorization": f"Bearer {AUTH_TOKEN}"}


def get_courier_by_id(courier_id):
    """Получает данные курьера по ID."""
    url = f"{BASE_URL}/couriers/{courier_id}"
    headers = _get_auth_header()
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def create_courier(data):
    """Создаёт нового курьера."""
    url = f"{BASE_URL}/couriers"
    headers = _get_auth_header()
    headers["Content-Type"] = "application/json"
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()


def delete_courier(courier_id):
    """Удаляет курьера по ID."""
    url = f"{BASE_URL}/couriers/{courier_id}"
    headers = _get_auth_header()
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    return response.json()