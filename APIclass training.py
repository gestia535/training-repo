# Прежде, чем писать тесты, необходимо создать архитектуру
# Она выглядит так: BaseAPI, Service, test
# Здесь создаем BaseAPI. В нем прописываются ручки, прикрепляются токены
import logging

import pytest
import requests
from requests import session

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)
# Базовая настройка логов: выводим время, уровень и сообщение. Благодаря getLogger(__name__)
# в логах сразу будет видно, какой класс отправил сообщение

class BaseAPI:
    def __init__(self, token=None):
        self.base_url = 'https://example.com'
        # Базовый URL лучше выносить в конфиг, но для примера, пропишем тут. Правильно будет так
        # class BaseAPI:
        #     def __init__(self, base_url):
        #         self.base_url = base_url  # Теперь мы можем тестировать разные стенды (dev, staging, prod)
        #         self.session = requests.Session()
        #
        # # В тесте:
        # api = UserAPI(base_url="https://example.com")

        self.session = requests.Session()
        # Используем библиотеку session, чтобы tcp соединение оставалось открытым при каждом запросе,
        # сохранялся токен и куки

        self.session.headers.update({"Content-Type": "application/json"})
        # Эта команда берет объект сессии и говорит ему: «Отныне во всех запросах, которые я буду делать
        # через тебя, автоматически добавляй в заголовок (HTTP Header) тип контента JSON». Точно так же одной строчкой
        # можно добавить токен, который нужен для 99% твоих тестов:
        # self.session.headers.update({"Authorization": f"Bearer {token}"})

        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})

        # Здесь, если токен передается мы добавляем его в заголовки сессии. Код метода _request не меняется, сессия сама
        # прикрепила токен. Далее, в тестах в фикстурах получаем токен 1 раз и передаем в другие сервисы.
        # Пример структуры теста с фикстурами:
        # В файле с тестами или conftest.py
        # @pytest.fixture(scope="session")
        # def auth_token():
        #     # Здесь логика получения токена через логин/пароль
        #     return "secret_abc_123"
        #
        # @pytest.fixture
        # def user_api(auth_token):
        #     # Создаем сервис и передаем в него токен
        #     return UserAPI(token=auth_token)
        #
        # def test_get_private_data(user_api):
        #     # Запрос уйдет уже с токеном и залогируется в консоли
        #     response = user_api.get_user(1)
        #     assert response.status_code == 200

    def _request(self, method, endpoint, **kwargs):
        """
                Универсальный метод для всех запросов.
                method: GET, POST, PUT, DELETE
                endpoint: путь (например, /users)
                kwargs: дополнительные параметры (json, params, headers)
                _method() — внутренний метод (используем только внутри самого класса).
                """
        url = f"{self.base_url}{endpoint}"

        logger.info(f"Sending {method} request to {url}. Payload: {kwargs.get('json')}")
        # Логируем исходящий запрос

        response = self.session.request(method, url, **kwargs)
        # Выполняем запрос в рамках одной сессии (session), сюда передается метод, переменная url, доп параметры

        logger.info(f"Response status: {response.status_code}. Data: {response.text}")
        # Логируем входящий ответ

        response.raise_for_status()
        # Этот метод выбрасывает ошибку, если сервер лежит, либо ошибка клиента (400-500)
        # Важный момент: этот метод будет мешать при негативных тестах. В этом случае, лучше добавить флаг raise_error
        # Пример с флагом:
        # В api/base_api.py
        # def _request(self, method, endpoint, raise_error=True, **kwargs):
        #     url = f"{self.base_url}{endpoint}"
        #     response = self.session.request(method, url, **kwargs)
        #
        #     if raise_error:
        #         response.raise_for_status()
        #
        #     return response
        #
        # # В api/user_api.py просто прокидываем этот флаг
        # def create_user(self, payload, raise_error=True):
        #     return self._request("POST", "/users", json=payload, raise_error=raise_error)
        # Негативный тест будет выглядеть так:
        #
        # def test_bad_request():
        #     api = UserAPI()
        #     # Говорим методу: "Не падай, я сам проверю статус"
        #     response = api.create_user(payload={}, raise_error=False)
        #     assert response.status_code == 400

        return response

class UserAPI(BaseAPI):
    def get_user(self, user_id):
        return self._request("GET", f"/users/{user_id}")

    def create_user(self, name, job):
        payload = {
            "name": name,
            "job": job
        }
        return self._request("POST", "/users", json=payload)

# Здесь мы создали Service класс для конкретного рута (/users). В сервисных классах происходит отправка запросов
# для подготовки к тестам. В идеальной структуре, фикстура вызывает методы сервисного класса.
# В противном случае, если поменяется название поля в АПИ, то нужно будет менять ее во всех фикстурах,
# а не в одном методе в сервисном классе.

# Далее, лучше всего создать тестовый класс, например class TestCreateUser и в нем прописать тесты + и - касающиеся
# создания юзеров.

class TestCreateUser:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.user_api = UserAPI()

    # Используем фикстуру для всего сета тестов в этом классе. Создаем объект класса UserAPI

    def test_create_user_success(self):
        response = self.user_api.create_user(name="Ivan", job="QA")
        assert response.status_code == 201
        assert response.json()["name"] == "Ivan"

    def test_create_user_empty_name(self):
        response = self.user_api.create_user(name="", job="QA", raise_error=False)
        assert response.status_code == 400
        assert "error" in response.json()

