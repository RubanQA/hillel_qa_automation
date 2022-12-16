# Занятия проходят по понедельникам и четвергам в 19:15. Первое занятие произошло 17.10.2022. Всего 32 занятия.

from datetime import *

start = datetime(2022, 10, 17, 19, 15)
start_str = start.strftime('%d %b %Y  %H:%M')
days3 = timedelta(days=3)
days4 = timedelta(days=4)

l = []

for i in range(32):
    start_str = start.strftime ('%d %b %Y %H:%M')
    if i % 2 == 0:
        l.append(f'Lecture {i+1:>3d}: {start_str}')
        start += days3
    else:
        l.append(f'Lecture {i+1:>3d}: {start_str}')
        start += days4
length = len(max(l, key=len))

for _ in l:
    print(_)