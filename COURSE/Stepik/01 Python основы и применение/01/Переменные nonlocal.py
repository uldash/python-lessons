# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 11:23:32 2018

@author: user
"""

ok_status = True


def f():
    ok_status = True
    vowels = ['a', 'u', 'i', 'e', 'o']

    def check(word):
        # global ok_status
        nonlocal ok_status
        for vowel in vowels:
            if vowel in word:
                return True
            ok_status = False
            return False

    print(check('abacaba'))  # True
    print(ok_status)  # True
    print(check('www'))  # False
    print(ok_status)  # False


f()
print(ok_status)

x, y = 1, 2


def foo():
    global y
    if y == 2:
        x = 2
        y = 1


foo()
print(x)
if y == 1:
    x = 3
print(x)
