# 1. Пользователь вводит с клавиатуры три числа в переменные a, b, c. Если все числа больше 10
# и первые два числа делятся на 3, то вывести YES, иначе NO
a = int(input())
b = int(input())
c = int(input())
if a > 10 and b > 10 and c > 10 and a % 3 == 0 and b % 3 == 0:
    print('Yes')
else:
    print('No')

# ver. 2
a, b, c = int(input()), int(input()), int(input())
print('Yes' if a > 10 and b > 10 and c > 10 and a % 3 == 0 and b % 3 == 0 else 'No')

# 2. Пользователь вводит с клавиатуры три числа в переменные a, b, c.
# Найдите наибольшее число из них и запишите в переменную max.
a, b, c = int(input()), int(input()), int(input())
if a > b > c:
    max = a
elif b > a > c:
    max = b
elif c > b > a:
    max = c

# 3. Пользователь вводит два числа A и B, нужно вывести сумму всех четных чисел в диапазоне от A до B.
a, b, = int(input()), int(input())
count = 0
for i in range(a, b+1):
    if i % 2 == 0:
        count += i
print(count)
