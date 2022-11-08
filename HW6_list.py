# 1. Запросить у пользователя 5 чисел и записать их в список
l = []
for i in range(5):
    l.append(int(input('Enter your number: ')))
print(l)

# 2. Дан список A = [1, 2, 3, 4, 5].Удалить последнее число из списка
A = [1, 2, 3, 4, 5]
A.pop()
print(A)

# v2
A = [1, 2, 3, 4, 5]
del A[-1]
print(A)

# 3. Запросить у пользователя 10 чисел и записать их в список A. Запросить у пользователя число N.
#Вывести пользователю сколько в списке A повторяется число N.
A = []
for i in range(10):
    A.append(int(input('Enter your number: ')))
N = int(input('Enter number to count: '))
print(f'Your count number is reapeat {A.count(N)} times')

# 4. Запросить у пользователя число N. Запросить у пользователя N чисел и записать их в список A.
# Вывести список в обратной последовательности
N = int(input('Enter number of list: '))
A = []
for i in range(N):
    A.append(int(input('Enter your number: ')))
A.reverse() # print(A[::-1])
print(A)

# 5. Запросить у пользователя 5 чисел и записать их в список A. Записать все числа из списка A которые больше 5 в список C
A = []
for i in range(5):
    A.append(int(input('Enter your number: ')))
C = [x for x in A if x > 5]
print(C)

# 6. Запросить у пользователя число N. Запросить у пользователя N целых чисел и записать их в список A.
# Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min, max, sorted, sort).
# Вывести эти числа.
N = int(input('Enter number of list: '))
A = []
for i in range(N):
    A.append(int(input('Enter your number: ')))
mini = A[0]
maxi = A[0]
for i in A:
    if i < mini:
        mini = i
    else:
        if i > maxi:
            maxi = i
print(f'Min number is: {mini}')
print(f'Max number is: {maxi}')

# 7. Пользователь вводит текст нужно вывести количество чисел в этом тексте.
text = input('Enter your text: ').split()
count = 0
for i in text:
    if i.isdigit():
        count += 1
if count > 0:
    print(f'Find {count} numbers')
else:
    print("Numbers not found")