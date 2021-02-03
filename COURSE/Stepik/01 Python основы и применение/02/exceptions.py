# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 10:00:34 2018

@author: user
"""


class EvenLightMixin:
    def even_length(self):
        return len(self) % 2 == 0


class MyList(list, EvenLightMixin):
    pass


ml = MyList([1, 12, 4, 17])
ml.sort()
print(ml)
