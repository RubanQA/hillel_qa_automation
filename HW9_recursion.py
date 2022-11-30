# 1. Написать функцию которая принимает целое число - number. Функция должна возвращать 'yes' если number
# является степенью двойки, иначе 'no'. Запрещено пользоваться функцией или оператором возведение в степень.

def is_power_of_two(num: int):
    num = num / 2
    if num == 2:
        print('YES')
    elif num > 2:
        return is_power_of_two(num)
    elif num == 0:
        print("Please enter a number bigger than 0!")
    else:
        print('NO')

is_power_of_two(256)
is_power_of_two(125)