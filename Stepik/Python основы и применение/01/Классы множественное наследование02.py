# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 15:49:45 2018

@author: user
"""

class A:
    pass

class B(A):
    pass

class C:
    pass

class D(C):
    pass


class F(A,B):
    pass 
class E(B, C, D):
    pass

#print(F.mro())
#print(E.mro())
