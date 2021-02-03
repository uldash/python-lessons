# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:57:17 2018

@author: user
"""

# Функция в качестве аргумента получает функцию
# и возвращает функцию


def D(f):
    # Вложенная функция
    # Вычисляет приближенное значение производной
    def df(x, dx=0.001):
        # результат вложенной функции
        return (f(x + dx) - f(x)) / dx

    # Результат функции - производная
    return df


def f1(x):
    return x**2


def f2(x):
    return 1 / (1 + x)


def show(F, Nmax, Xmax, dx, f):
    for i in range(Nmax + 1):
        x = i * Xmax / Nmax
        print(F(x), F(x, dx), f(x), sep=" -> ")


F1 = D(f1)
F2 = D(f2)
print("Производная (х**2)' = 2x:")
show(F1, 5, 1, 0.01, lambda x: 2 * x)
print("Производная (1(1+x))' = -1/(1+x)**2:")
show(F2, 5, 1, 0.01, lambda x: -1 / (1 + x)**2)
