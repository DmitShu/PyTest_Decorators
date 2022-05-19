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

writing_tests()