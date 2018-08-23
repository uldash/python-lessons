# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 11:58:29 2018

@author: user
"""

from random import *

def rand_matrix(n,m):
    A=[[randint(0,9) for j in range(m)] for i in range(n)]
    return A

def unit_matrix(n):
    #Единичная матрица
    A=[[int(i==j) for i in range(n)] for j in range(n)]
    return A

def mult_matrix(A,B):
    n=len(A)
    C=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j]+=A[i][k]*B[k][j]
    return C
def show_matrix(A):
    for a in A:
        for b in a:
            print(b,end=" ")
        print()
seed(2014)
A=rand_matrix(3,5)
print("Список:",A)
print("Эта же матрица:")
show_matrix(A)

E=unit_matrix(4)
print("Единичная матрица:")
show_matrix(E)

A1=rand_matrix(3,3)
A2=rand_matrix(3,3)
A3=mult_matrix(A1,A2)
print("Первая матрица:")
show_matrix(A1)
print("Вторая матрица:")
show_matrix(A2)
print("Произведение матриц:")
show_matrix(A3)