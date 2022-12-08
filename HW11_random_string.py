# 1. Написать функцию, которая возвращает слуайную строку заданной длины.
# Строка должна состоять из больших и маленьких латинских букв и цифр.
# Ограничения:
# - Не использовать модуль string
# - Не создавать руками список ['a', 'b', 'c', ..., 'X', 'Y', 'Z', 0, 1, ..., 8, 9]

from random import randint, choice


def get_random_string(length: int) -> str:
    list_char = []
    random_string = ''
    for i in range(length):
        list_char.append(chr(randint(65, 90)))  # Upper letters
        list_char.append(chr(randint(97, 122)))  # Lower letters
        list_char.append(chr(randint(48, 57)))  # Numbers
        random_char = choice(list_char)
        random_string += random_char
    return random_string


print(get_random_string(10))
