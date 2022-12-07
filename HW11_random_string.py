# 1. Написать функцию, которая возвращает слуайную строку заданной длины.
# Строка должна состоять из больших и маленьких латинских букв и цифр.
# Ограничения:
# - Не использовать модуль string
# - Не создавать руками список ['a', 'b', 'c', ..., 'X', 'Y', 'Z', 0, 1, ..., 8, 9]

import random


def get_random_string(length: int) -> str:
    r_string = ""
    for i in range(length):
        numbers = chr(random.randint(48, 57))
        char_upper = chr(random.randint(97, 123))
        char_lower = chr(random.randint(65, 91))
        r_string += char_upper + char_lower + numbers
    return r_string


print(get_random_string(5))
