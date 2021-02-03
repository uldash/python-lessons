# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 14:37:00 2018

@author: user
"""

# Решение квадратного уравнения
# на множествах действительных и комплексных чисел

from math import sqrt


class LinearEquationWarning(Warning):
    def __init__(self, b, c):
        try:
            self.x = -c / b
        except ZeroDivisionError:
            if c == 0:
                self.x = "любое число"
            else:
                self.x = "решений нет"

    def __str__(self):
        txt = "Решение уравнения: "
        txt += str(self.x)
        return txt


class ComplexRootError(Exception):
    def __init__(self, a, b, D):
        self.x1 = complex(-b / 2 / a, sqrt(-D) / 2 / a)
        self.x2 = complex(-b / 2 / a, -sqrt(-D) / 2 / a)

    def __str__(self):
        txt = "x1 =" + str(self.x1) + "\n"
        txt += "x2 =" + str(self.x2)
        return txt


def show_params(a, b, c):
    print("Параметры: a={0}, b={1}, c={2}".format(a, b, c))


def find_roots(a, b, c):
    show_params(a, b, c)
    try:
        if a == 0:
            raise LinearEquationWarning(b, c)
        D = b * b - 4 * a * c
        if D < 0:
            raise ComplexRootError(a, b, D)
        x1 = (-b + sqrt(D)) / 2 / a
        x2 = (-b - sqrt(D)) / 2 / a
        print("x1 =", x1)
        print("x2 =", x2)
    except LinearEquationWarning as err:
        print("Это линенйное уравнение!")
        print(err)
    except ComplexRootError as err:
        print("Внимание! Решения комплексные!")
        print(err)


print("Решение уравнения a*x**2+b*x+c=0.")
# Два действительных корня
find_roots(2, -3, 1)
# Совпадающие корни
find_roots(1, 2, 1)
# Два комплесных корня
find_roots(2, 1, 3)
# Линейное уравнение с одним решением
find_roots(0, -6, 5)
# Решений нет
find_roots(0, 0, 1)
# Решение - любое число
find_roots(0, 0, 0)
