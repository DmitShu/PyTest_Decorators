import functools
from datetime import datetime

def my_decorator(func):
    def wrapper():
        print("Начало выполнения функции.")
        func()
        print("Конец выполнения функции.")

    return wrapper

def my_first_decorator():
	print("Это мой первый декоратор!")

my_first_decorator = my_decorator(my_first_decorator)

# my_first_decorator()

def working_hours(func):
    def wrapper():
        if 9 <= datetime.now().hour < 21:
            func()
        else:
            pass  # Нерабочее время, выходим
    return wrapper

@working_hours
def writing_tests():
    print("Я пишу тесты на python!")

# writing_tests = working_hours(writing_tests)

# writing_tests()

# def do_twice(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper

def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@do_twice
def test_twice_without_params():
    print("Этот вызов без параметров")


@do_twice
def test_twice_2_params(str1, str2):
    print("В этой функции 2 параметра - {0} и {1}".format(str1, str2))

@do_twice
def test_twice(str):
    print("Этот вызов возвращает строку {0}".format(str))

# test_twice_without_params()
# test_twice_2_params("один", "два")
# test_twice("single")

@do_twice
def test_twice_2(str):
    print("Этот вызов возвращает строку {0}".format(str))
    return "Done"

decorated_value = test_twice_2("single")
print(decorated_value)

@do_twice
def test_twice(str):
    print("Этот вызов возвращает строку {0}".format(str))
    return "Done"

print(test_twice.__name__)

def debug(func):
    """Выводит сигнатуру функции и возвращаемое значение"""
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Вызываем {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} вернула значение - {value!r}")
        return value
    return wrapper_debug

@debug
def age_passed(name, age=None):
  if age is None:
    return "Необходимо передать значение age"
  else:
    return "Аргументы по умолчанию заданы!"

age_passed("Роман")
age_passed("Роман", age=21)