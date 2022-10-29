# 1. Пользователь вводит с клавиатуры три числа в переменные a, b, c. Если все числа больше 10
# и первые два числа делятся на 3, то вывести YES, иначе NO
a = int(input('Enter number A: '))
b = int(input('Enter number B: '))
c = int(input('Enter number C: '))
if a > 10 and b > 10 and c > 10 and a % 3 == 0 and b % 3 == 0:
    print('Yes')
else:
    print('No')

# ver. 2
a, b, c = int(input('Enter number A: ')), int(input('Enter number B: ')), int(input('Enter number C: '))
print('Yes' if a > 10 and b > 10 and c > 10 and a % 3 == 0 and b % 3 == 0 else 'No')

# 2. Пользователь вводит с клавиатуры три числа в переменные a, b, c.
# Найдите наибольшее число из них и запишите в переменную max.
a, b, c = int(input('Enter number A: ')), int(input('Enter number B: ')), int(input('Enter number C: '))
if a == b == c:
    print('Numbers must be different! Please try again!')
elif a > b and a > c:
    max = a
elif b > a and b > c:
    max = b
elif c > b and c > a:
    max = c
print(max)

# 3. Пользователь вводит два числа A и B, нужно вывести сумму всех четных чисел в диапазоне от A до B.
a, b, = int(input('Enter number A: ')), int(input('Enter number B: '))
count = 0
if a == b:
    print('Numbers must be different! Please try again!')
for i in range(a, b+1):
    if i % 2 == 0:
        count += i
print(count)