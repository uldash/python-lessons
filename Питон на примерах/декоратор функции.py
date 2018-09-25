# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 17:14:27 2018

@author: user
"""

from math import exp, sin, cos, tan


# Функция для использования в декораторе
def F(f):
    res = lambda x: exp(-f(x)**2)
    return res


# Функция для использования в декораторе
def Q(f):
    def q(x):
        return tan(f(x))

    return q


@F  # Декоратор
def f(x):
    return sin(x)


@F  # Декоратор
def g(x):
    return cos(x)


@Q
@F  # Декоратор
def h(x):
    return x


# Переменная
n = 5
# Значения функций в разных точках
print("Функция f():")
for i in range(n + 1):
    z = i / n
    # F(f)(z) без декоратора @F даст тот же результат
    print(f(z), "->", exp(-sin(z)**2))
print("Функция g():")
for i in range(n + 1):
    z = i / n
    print(g(z), "->", exp(-cos(z)**2))
print("Функция h():")
for i in range(n + 1):
    z = i / n
    print(h(z), "->", tan(exp(-z**2)))
