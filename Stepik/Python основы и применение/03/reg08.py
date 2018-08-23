'''Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
Sample Input:

zabcz
zzz
zzxzz
zz
zxz
zzxzxxz
Sample Output:

zabcz
zzxzz
'''
import sys
import re

#pattern = r"z\w{3}z"
pattern = r"z...z"
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)