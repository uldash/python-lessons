# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 15:12:55 2018

@author: user
"""

class D:pass
class E:pass
class B(D,E):pass
class C:pass
class A(B,C):pass

print(issubclass(A,A))
print(issubclass(C,D))
print(issubclass(A,D))
print(issubclass(C,object))
print(issubclass(object,C))

x=A()
print(isinstance(x,A))

#Класс примесь
class EventLengthMixin:
    def even_length(self):
        return len(self)%2==0
class MyList(list,EventLengthMixin):
    pass
class MyDict(dict,EventLengthMixin):
    pass

print(MyList.mro())
x=MyList([1,2,3])
print(x.even_length())
x.append(4)
print(x.even_length())

y=MyDict()
y['key']='value'
y['another key']='another value'
print(y.even_length())