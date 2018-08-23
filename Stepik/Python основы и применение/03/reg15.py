'''
Вам дана последовательность строк.
Выведите строки, содержащие двоичную запись числа, кратного 3.

Двоичной записью числа называется его запись в двоичной системе счисления.

Примечание 2:
Данная задача очень просто может быть решена приведением строки к целому числу и проверке 
остатка от деления на три, но мы все же предлагаем вам решить ее, не используя приведение к числу.
Sample Input:

0
10010
00101
01001
Not a number
1 1
0 0
Sample Output:

0
10010
01001
'''
import sys
import re

pattern = r"^((((0+)?1)(10*1)*0)(0(10*1)*0|1)*(0(10*1)*(1(0+)?))|(((0+)?1)(10*1)*(1(0+)?)|(0(0+)?)))$"
for line in sys.stdin:
    line = line.rstrip()
    x = re.search(pattern, line)
    if x:
        print(x.group())
'''
import re
import sys

pattern = "^(0|(1(01*0)*1))*$"
pattern = re.compile(pattern)
for line in sys.stdin:
    line = line.rstrip()
    if pattern.match(line):
        print(line)
'''