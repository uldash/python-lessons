# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 15:46:40 2018

@author: user
"""

class A:
   def foo(self):
      print("A")

class B(A):
   pass

class C(A):
   def foo(self):
      print("C")

class D:
   def foo(self):
      print("D")

class E(B, C, D):
   pass

print(E.mro())
E().foo()