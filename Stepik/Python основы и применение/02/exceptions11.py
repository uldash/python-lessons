# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 16:33:38 2018

@author: user
"""
GREETING = 'Hellow, '


class BadName(Exception):
    pass


def greet(name):
    if name[0].isupper():
        return "Hello, "+name
    else:
        raise BadName(name+' is inappropriate name')


# Проверяем, вызвали скрипт как программу или импортировали как модуль
# При импорте __name__=='имя файла'
__all__ = ['BadName', 'greet']
if __name__ == '__main__':
    print('Import is execution')
