# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 16:52:40 2018

@author: user
"""

A=[1,30,"text",True,30,100,False]
print("Список А:",A)
B=set(A)
print("Множество В:",B)
C={1,30,"text",True,30,100,False}
print("Множество С:",C)
print("Равенство множеств:",B==C)
print("Элемент 1 в множестве С:",1 in C)

#Объединение множеств
print("Объединение множеств")
A={1,2,3,4}
print("Множество А:",A)
B={3,4,5,6}
print("Множество B:",B)
C=A|B
print("Множество С=А|В:",C)
print("Множество A.union(B):",A.union(B))
print("Множество B.union(A):",B.union(A))
A.update(B)
print("Множество А:",A)
B=B|{-1,-2,-3}
print("Множество B:",B)

#Пересечение множеств
print("Пересечение множеств")
A={1,2,3,4}
print("Множество А:",A)
B={3,4,5,6}
print("Множество B:",B)
C=A&B
print("Множество C=A&B:",C)
print("Множество A.intersection(B):",A.intersection(B))
print("Множество B.intersection(A):",B.intersection(A))
A.intersection_update(B)
print("Множество A:",A)
B=B&{4,6,8,10}
print("Множество B:",B)
C&={1,2,3}
print("Множество C:",C)

#Разность множеств
print("Разность множеств")
A={1,2,3,4}
B={3,4,5,6}
print("Множество А:",A)
print("Множество B:",B)
C=A-B
print("Множество С=A-B",C)
print("Множество A.difference(B):",A.difference(B))
print("Множество B.difference(A):",B.difference(A))
A.difference_update(B)
print("Множество А:",A)
B=B-{4,6,8,10}
print("Множество B:",B)
C-={1,3,5}
print("Множество C:",C)

#Симметрическая разность множеств
print("Симметрическая разность множеств")
A={1,2,3,4}
B={3,4,5,6}
print("Множество А:",A)
print("Множество B:",B)
C=A^B
print("Множество С=A^B:",C)
print("Множество A.symmetric_difference(B):",A.symmetric_difference(B))
print("Множество B.symmetric_difference(A):",B.symmetric_difference(A))
A.symmetric_difference_update(B)
print("Множество А:",A)
B=B^{4,6,8,10}
print("Множество B:",B)
C^={1,3,5}
print("Множество C:",C)

print("Генератор множеств")
A={x for x in range(1,101) if (x%5==2 or x%5==4) and x%7==3 and x%3!=1}
print(A)