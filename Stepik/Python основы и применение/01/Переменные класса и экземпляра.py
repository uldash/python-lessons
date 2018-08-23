# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 12:50:22 2018

@author: user
"""

#Плохой пример
class Song:
    tags=[]#Так не надо
    def __init__(self,artist,song):
        self.artist=artist
        self.song=song
    def add_tegs(self,*args):
        self.tags.extend(args)
    
song1=Song('AAAA','BBBB')
song1.add_tegs('CCCC','DDDD')
song2=Song('EEEE','FFFF')
song2.add_tegs('GGGG','HHHH')
print(song2.tags)#Tags общий

class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


a = A()
b = A()

a.bar()
a.foo()

c = A()

print(a.val)
print(b.val)
print(c.val)