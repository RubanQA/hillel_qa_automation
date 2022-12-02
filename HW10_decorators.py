# 1. Написать декоратор call_times, который будет принимать в качестве параметра file_name, считать
# количество вызовов функций и записывать в файл в формате f'{func_name} была вызвана {count} раза.\n'

def call_times(file_name):
    def decorator(function):
        def wrapper(*args, **kwargs):
            wrapper.counter += 1
            with open(file_name, 'w') as file:
                file.write(f'{function.__name__} была вызвана {wrapper.counter} раз(а).\n')
            return function

        wrapper.counter = 0
        return wrapper

    return decorator


@call_times('files/foo.txt')
def foo():
    pass


@call_times('files/foo.txt')
def boo():
    pass


@call_times('files/calls.txt')
def doo():
    pass


foo()
boo()
foo()
foo()
boo()
doo()
