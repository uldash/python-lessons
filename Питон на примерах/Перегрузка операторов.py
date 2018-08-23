# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:50:00 2018

@author: user
"""
from math import sqrt

class Vector:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        txt="<"+str(self.x)+" | " + str(self.y)+" | " + str(self.z)+">"
        return txt
    def __add__(self,obj):
        t=Vector()
        t.x=self.x+obj.x
        t.y=self.x+obj.y
        t.z=self.x+obj.z
        return t
    def __iadd__(self,obj):
        self=self+obj
        return self
    def __mul__(self,p):
        if type(p)==Vector:
            res=self.x*p.x+self.y*p.y+self.z*p.z
            return res
        else:
            self.x*=p
            self.y*=p
            self.z*=p
            return self
    def __rmul__(self,p):
        return self*p
    def __neg__(self):
        return Vector(-self.x,-self.y,-self.z)
    def __sub__(self,obj):
        return -obj+self
    def __isub__(self,obj):
        self=-obj+self
        return self
    def __abs__(self):
        return sqrt(self*self)
    def __truediv__(self,p):
        return self*(1/p)
    def __eq__(self,obj):
        if self.x==obj.x and self.y==obj.y and self.z==obj.z:
            return True
        else:
            return False
    def __ne__(self,obj):
        return not self==obj
    def __lt__(self,obj):
        if abs(self)<abs(obj):
            return True
        else:
            return False
    def __le__(self,obj):
        if abs(self)<=abs(obj):
            return True
        else:
            return False
    def __qe__(self,obj):
        if abs(self)>=abs(obj):
            return True
        else:
            return False
    def __invert__(self):
        self.x=10-self.x
        self.y=10-self.y
        self.z=10-self.z
        return self
    def __lshift__(self,n):
        for i in range(n):
            self.x,self.y,self.z=self.y,self.z,self.x
        return self
    def __rlshift__(self,n):
        return self>>n
    def __rshift__(self,n):
        for i in range(n):
            self.x,self.y,self.z=self.z,self.x,self.y
        return self
    def __rrshift__(self,n):
        return self<<n
   
print("Векторы:")
a=Vector(1,2,-1)
b=Vector(1,-1,3)
c=~Vector(9,8,11)
print("a =",a)
print("b =",b)
print("c =",c)
print("Сравнение векторов.")
print("a==b ->",a==b)
print("a!=b ->",a!=b)
print("a==c ->",a==c)
print("a<b ->",a<b)
print("a>b ->",a>b)
print("a<=c ->",a<=b)
print("a>=c ->",a>=b)
print("Сумма векторов.")
print("a+b =",a+b)
c+=a
print("c+=a ->",c)
print("Разность векторов.")
print("a-b =",a-b)
c-=a
print("c-=a ->",c)
print("Умножение векторов.")
print("a*b =",a*b)
print("Умножение и деление вектора на число:")
print("a*b =",a*b)
print("a =",a)
print("2*b =",2*b)
print("b =",b)
print("-b =",-b)
print("b =",b)
print("a/3 =",a/3)
print("a =",a)
print("Циклические перестановки:")
v=Vector(1,2,3)
print("v =",v)
print("v<<1 =",v<<1)
print("v>>1 =",v>>1)
print("2>>v =",2>>v)
print("2<<v =",2<<v)