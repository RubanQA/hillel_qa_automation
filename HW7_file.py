# 1. Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers.
# Preconditions
my_file = open("files/file1.txt", "w+")
my_file.write("Viv1amu2s co4ndime1ntum in pu2rus id tr4ist8ique")
my_file.close()
import random

f = open('files/file1.txt', 'r')
file_data = f.read()
for i in file_data:
    if not i.isdigit():
        file_data = file_data.replace(i, ' ')
numbers = [i for i in file_data.split(' ') if i.isdigit()]
print(numbers)
f.close()

# 2. Запросить у пользователя текст и записать его в файл data.txt
# Preconditions
my_file1 = open("files/data.txt", "w+")
my_file1.close()

text = input('Please, enter your text: ')
with open('files/data.txt', 'w') as f:
    f.write(text)
    f.close()

# 3. Запросить у пользователя число N и запросить N чисел у пользователя, потом записать их в файл numbers.txt через пробел
# Preconditions
num_file = open("files/numbers.txt", "w+")
num_file.close()

with open('files/numbers.txt', 'w') as f:
    N = int(input("Please, enter count your numbers: "))
    for i in range(N):
        numbers = input('Enter your number: ')
        f.write(numbers + ' ')

# 4. Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число
#Preconditions
r_file = open("files/random_numbers.txt", "w+")
r_file.close()

import random

r_num = [str(random.randint(1, 100)) + "\n" for _ in range(100)]
with open('files/random_numbers.txt', 'w') as f:
    f.writelines(r_num)
f.close()

# 5. Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю
#Preconditions
r_file = open("files/random_text.txt", "w+")
r_file.close()

with open('files/random_text.txt', 'rt') as f:
    text = f.read()
    words = text.split()
print('Number of words in text file :', len(words))
f.close()

# 6. Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел
#Preconditions
file = open("files/numbers_with_space.txt", "w+")
file.close()

f = open('files/numbers_with_space.txt')
summa = [int(i) for i in f.read().split(' ')]
print(sum(summa))
f.close()

# 7. Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются
#Preconditions
file = open("files/top_5_strings.txt", "w+")
file.close()

from collections import Counter

f = open("files/top_5_strings.txt")
top_five = f.read().split()
c = Counter(top_five)
top_list = c.most_common(5)
print(* top_list)


# f = open('random_numbers.txt')
# while True:
#     line = f.readline()
#     if len(line) == 0:
#         break
#     print(line, end='')