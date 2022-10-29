# 1. Вывести треугольник #1 с шириной N с помощью цикла while
n = int(input('Please enter width N: '))
i = n
while i > 0:
  print(i * '*')
  i -= 1

# 2. Вывести треугольник #2 с шириной N с помощью цикла while
n = int(input('Please enter width N: '))
i = 1
while i <= n:
  print(i * '*')
  i += 1

# 3. Вывести треугольник #3 с шириной N с помощью цикла while
n = int(input('Please enter width N: '))
i = n
while i > 0:
  print(' '*(n-i) + '*' * i)
  i -= 1

# 4. Вывести треугольник #4 с шириной N с помощью цикла while
n = int(input('Please enter width N: '))
i = 1
while i <= n:
  print(' '*(n-i) + '*' * i)
  i += 1