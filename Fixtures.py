import pytest
import requests
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

@pytest.fixture()
def get_key():
    response = requests.post(url='https://petfriends1.herokuapp.com/login',
                             data={"email": email, "pass": password})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    return response.request.headers.get('Cookie')

def test_getAllPets(get_key):
    response = requests.get(url='https://petfriends1.herokuapp.com/api/pets',
                            headers={"Cookie": get_key})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'