import pytest
import requests
import sys
from datetime import datetime

email = "Test19856@Test19856"
password = "Test19856"

# function — запускается для каждого теста по умолчанию любая фикстура имеет scope=«function»;
# class — запускается для каждого тестового класса;
# module — запускается для каждого модуля;
# package — запускается для каждого пакета;
# session — запускается один раз перед всеми тестами.


# @pytest.fixture(scope="class", autouse=True)
# def session_fixture():
#     print("\nclass fixture starts")
#
# @pytest.fixture(scope="function", autouse=True)
# def function_fixture():
#     print("\nfunction fixture starts")
#
#
# class TestClass23:
#
#     def test_first(self):
#         pass
#
#     def test_second(self):
#         pass


@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print (f"\nТест шел: {end_time - start_time}")

@pytest.fixture()
def some_data():
    return 42

def test_some_data(some_data):
    assert some_data == 42


# @pytest.fixture()
# def get_key():
#     response = requests.post(url='https://petfriends1.herokuapp.com/login',
#                              data={"email": email, "pass": password})
#     assert response.status_code == 200, 'Запрос выполнен неуспешно'
#     assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
#     return response.request.headers.get('Cookie')
#
# def test_getAllPets(get_key):
#     response = requests.get(url='https://petfriends1.herokuapp.com/api/pets',
#                             headers={"Cookie": get_key})
#     assert response.status_code == 200, 'Запрос выполнен неуспешно'
#     assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'


@pytest.fixture(scope="class")
def get_key(request):

    response = requests.post(url='https://petfriends1.herokuapp.com/login',
                             data={"email": email, "pass": password})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    print("\nreturn auth_key")
    return response.request.headers.get('Cookie')


@pytest.fixture(autouse=True)
def request_fixture(request):
    if 'Pets' in request.function.__name__:
        print(f"\nЗапущен тест из сьюта Дом Питомца: {request.function.__name__}")


class TestClassPets:

    @pytest.mark.xfail(reason="сайт сдох")
    def test_getAllPets2(self, get_key):
        response = requests.get(url='https://petfriends1.herokuapp.com/api/pets',
                                headers={"Cookie": get_key})
        assert response.status_code == 200, 'Запрос выполнен неуспешно'
        assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'

    @pytest.mark.xfail(reason="сайт сдох")
    def test_getMyPets2(self, get_key):
        response = requests.get(url='https://petfriends1.herokuapp.com/my_pets',
                                headers={"Cookie": get_key})
        assert response.status_code == 200, 'Запрос выполнен неуспешно'
        assert response.headers.get('Content-Type') == 'text/html; charset=utf-8'

    def test_anotherTest(self):
        pass

minversion = pytest.mark.skipif(sys.version_info > (3, 6), reason="at least mymodule-1.1 required")

@minversion
def test_python36_and_greater():
    pass

@pytest.mark.api
@pytest.mark.auth
def test_auth_api():
   pass

@pytest.mark.ui
@pytest.mark.auth
def test_auth_ui():
   pass

@pytest.mark.api
@pytest.mark.event
def test_event_api():
   pass

@pytest.mark.ui
@pytest.mark.event
def test_event_ui():
   pass

# pytest Fixtures.py -v -m "api"