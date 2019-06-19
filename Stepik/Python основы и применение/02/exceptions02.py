# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 10:30:28 2018

@author: user
"""


def f(x, y):
    try:
        return x/y
    # except TypeError:
    #    print('Type error')
    # except ZeroDivisionError:
    #    print('Zero Division :(')
    except (TypeError, ZeroDivisionError) as err:
        print(type(err))
        print(err)
        print(err.args)


f(5, [])
print(f(5, 0))
