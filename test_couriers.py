"""
Тесты для процедурных хелперов из helpers.py.
Необъодимо переписать их под использование класса CourierAPIClient.
"""
import os

import pytest
import requests
from dotenv import load_dotenv

from api_client import CourierAPIClient


load_dotenv()


@pytest.fixture
def client():
    return CourierAPIClient(
        os.getenv("API_BASE_URL"),
        os.getenv("AUTH_TOKEN")
    )


@pytest.fixture
def new_courier_data():
    """Данные для создания нового курьера."""
    return {
        "first_name": "Мария",
        "last_name": "Сидорова",
        "phone": "+79997654321"
    }


@pytest.mark.usefixtures("fake_server")
class TestCourierHelpers:
    """Тесты для CourierAPIClient."""

    def test_get_courier_by_id(self, client):
        """Получение курьера с id=1 (зашит в fake_api)."""
        courier = client.get_courier_by_id(1)
        assert courier["id"] == 1
        assert courier["first_name"] == "Иван"

    def test_create_courier(self, client, new_courier_data):
        """Создание нового курьера."""
        result = client.create_courier(new_courier_data)
        assert "id" in result
        assert result["first_name"] == "Мария"

    def test_get_nonexistent_courier_raises(self, client):
        """Запрос несуществующего курьера вызывает ошибку 404."""
        with pytest.raises(requests.exceptions.HTTPError):
            client.get_courier_by_id(99999)

    def test_delete_courier(self, client):
        """Удаление курьера с id=2 (зашит в fake_api)."""
        result = client.delete_courier(2)
        assert result == {"status": "deleted"}