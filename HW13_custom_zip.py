# 3. Написать функцию, которая принимает несколько итерируемых объектов, и возвращает список из кортежей составленных из
# элементов итерируемых объектов одного индекса.
# Функция также должна принимать параметры с дефолтными значения:
# full=False - по умолчанию "склеить" последовательности по кратчайшей, иначе по самой длинной
# default=None - если full=True, вместо недостающих элементов поставить значение указанное в параметре default

from typing import Iterable, List, Tuple


def custom_zip(*sequences: Iterable, full=False, default=None) -> List[Tuple]:
    max_sequences = max(*sequences, key=len)
    min_sequences = min(*sequences, key=len)
    list_tuple = [[] for x in max_sequences]
    for i in range(len(sequences)):
        for k in range(len(list_tuple)):
            if k < len(sequences[i]):
                list_tuple[k].append(sequences[i][k])
            else:
                list_tuple[k].append(default)
    if full:
        return [tuple(i) for i in list_tuple]
    else:
        return [tuple(i) for i in list_tuple[:len(min_sequences)]]


seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
print(custom_zip(seq1, seq2))
print(custom_zip(seq1, seq2, full=True, default="Q"))
