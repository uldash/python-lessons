# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 23:37:52 2018

@author: user
"""


class MyList(list):
    def __getitem__(self, index):
        if index < 0:
            raise IndexError("list index out of range")
        return super(MyList, self).__getitem__(index)


def printmatrix(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if j == len(a[0]) - 1:
                print(a[i][j], end='')
            else:
                print(a[i][j], '', end='')
        print()


def up(i, j):
    return i - 1, j


def down(i, j):
    return i + 1, j


def left(i, j):
    return i, j - 1


def right(i, j):
    return i, j + 1


n = int(input())
a = MyList([0 for j in range(n)] for i in range(n))
b = ['right', 'down', 'left', 'up']
d = list(i for i in range(1, n**2 + 1))
napr = 0
scht_napr = 0
i = 0
j = 0
a[i][j] = d[0]
k = 1
while k <= n**2:
    if b[napr] == 'left':
        di, dj = left(i, j)
    elif b[napr] == 'down':
        di, dj = down(i, j)
    elif b[napr] == 'right':
        di, dj = right(i, j)
    elif b[napr] == 'up':
        di, dj = up(i, j)
    try:
        if a[di][dj] != 0:
            raise
        a[di][dj] = d[k]
        i = di
        j = dj
        k += 1
        scht_napr = 0
    except:
        napr = (napr + 1) % 4
        #print(b[napr])
        if scht_napr > 4:  #если 4 раза подрят повернулись, но не сдвинулись - выходим
            break
        scht_napr += 1
    #printmatrix(a)

printmatrix(a)
#print(d)