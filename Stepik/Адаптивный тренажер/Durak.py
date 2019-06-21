'''A durak deck contains 36 cards. Each card has a suit of either clubs, diamonds, hearts, or spades (denoted C, D, H, S). Each card also has a value of either 6 through 10, jack, queen, king, or ace (denoted 6, 7, 8, 9, 10, J, Q, K, A). For scoring purposes card values are ordered as above, with 6 having the lowest and ace the highest value.

Напишите программу, которая определяет, бьёт ли одна карта другую.
Если встречаются две карты одной масти, то побеждает та, у которой выше значение;
Если карты разных мастей, то карта, имеющая козырную масть, побеждает;
Если карты разных мастей и нет козырных, то никто не побеждает.

Формат ввода:
На первой строке через пробел указываются две карты в формате <значение><масть>, а на следующей строке указывается козырная масть.

Формат вывода:
Программа должна вывести слово 
First, если первая карта бьёт вторую, 
Second, если вторая карта бьёт первую,
Error, если ни одна из карт не может побить другую.

Sample Input 1:

AH JH
D
Sample Output 1:

First
Sample Input 2:

AH JS
S
Sample Output 2:

Second
Sample Input 3:

7C 10H
S
Sample Output 3:

Error
'''


val = ('6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

First, Second = input().split()
First = (First[:-1], First[-1])
Second = (Second[:-1], Second[-1])
Mast = input()

if First[1] == Second[1]:
    if val.index(First[0]) > val.index(Second[0]):
        print('First')
    else:
        print('Second')
elif First[1] == Mast and Second[1] != Mast:
    print('First')
elif First[1] != Mast and Second[1] == Mast:
    print('Second')
elif First[1] == Mast and Second[1] == Mast:
    if val.index(First[0]) > val.index(Second[0]):
        print('First')
    else:
        print('Second')
else:
    print('Error')
