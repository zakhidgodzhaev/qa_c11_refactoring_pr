"""
Фикстура для автоматического запуска fake_api перед тестами.
Сервер стартует в отдельном потоке и глушится после прогона тестов.
Не менять этот файл.
"""
import threading
import time
import pytest
from fake_api import app


@pytest.fixture(scope="session")
def fake_server():
    """Запускает fake_api на порту 5001."""
    server_thread = threading.Thread(
        target=app.run,
        kwargs={"port": 5001, "debug": False, "use_reloader": False},
        daemon=True,
    )
    server_thread.start()
    time.sleep(0.5)
    yield