# -*- coding: utf-8 -*-
"""
Created on Thu May 31 17:32:36 2018

@author: user
"""

print("Проверяем содержимое списка:")
myList=[1,3+2j,True,4.0]
#myList=[1,3+2j,"Python",4.0]
print("Список:",myList)
for s in myList:
    if type(s)==str:
        print("В списке есть текстовые элементы!")
        break
else:
    print("В списке нет текстовых элементов!")
print("End.")