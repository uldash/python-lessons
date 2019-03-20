'''Кодирование длин серий — это базовый алгоритм сжатия данных.

В этой задаче мы реализуем одну из самых простых его вариантов.

На вход алгоритму подаётся строка, содержащая символы латинского алфавита. 
Эта строка разбивается на группы одинаковых символов, 
идущих подряд ("серии"). Каждая серия характеризуется повторяющимся символом и 
количеством повторений. Именно эта информация и 
записывается в код: сначала пишется длина серии повторяющихся символов, затем 
сам символ. У серий длиной в один символ количество повторений будем опускать.
Например, рассмотрим строку

aaabccccCCaB
Разобъём её на серии
aaa b cccc CC a B
После чего закодируем серии и получим итоговую строку, которую и будем считать
 результатом работы алгоритма.
3ab4c2CaB
Формат ввода:
Одна строка, содержащая произвольные символы латинского алфавита.

Формат вывода:
Строка, содержащая закодированную последовательность.

Sample Input 1:

aaabccccCCaB
Sample Output 1:

3ab4c2CaB
Sample Input 2:

a
Sample Output 2:

a
'''
from itertools import groupby


def split_encode_series(text):
    lst = [list(g) for k, g in groupby(text)]
    for i in lst:
        yield (len(i), i[0])


def encode_series(series):
    res = ''
    for s in series:
        if s[0] > 1:
            res += str(s[0]) + s[1]
        else:
            res += s[1]
    return res


def rle_encode(text):
    return encode_series(list(split_encode_series(text)))


print(rle_encode(input().strip()))
