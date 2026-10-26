"""
Здесь должен быть создан класс CourierAPIClient.

Требования к классу:
- Конструктор __init__(self, base_url: str, auth_token: str)
- Приватный метод _get_auth_header(self)
- Публичные методы:
  - get_courier_by_id(self, courier_id: int)
  - create_courier(self, data: dict)
  - delete_courier(self, courier_id: int)
"""