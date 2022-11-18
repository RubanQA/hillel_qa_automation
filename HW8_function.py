# 1. Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.

def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

print(change([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 2. Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый
# элемент списка является и ключом и значением. Предполагается, что элементы списка будут
# соответствовать правилам задания ключей в словарях.

def to_dict(lst):
    return {key: key for key in lst}

print(to_dict(["Denis",  "Igor","Max"]))

# 3. Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start»
# до величины «end» включительно. Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

def sum_range(start, end):
    if start > end:
        end, start = start, end
    return sum(range(start, end + 1))

print(sum_range(1, 10))

# 4. Напишите функцию read_last(lines, file.txt), которая будет открывать определенный файл file.txt и выводить
# на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).

def read_last(lines, file):
        with open("files/file.txt", 'r') as f:
            f_lines = f.readlines()[-int(lines):]
        if lines > 0:
            for i in f_lines:
                print(i.strip())
        else:
            print('Please, enter number of lines more than 0!')

read_last(3, "files/file.txt")