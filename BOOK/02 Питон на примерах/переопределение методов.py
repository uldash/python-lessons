# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:58:48 2018

@author: user
"""


class BaseClass:
    def __init__(self, num):
        self.id = num

    def get(self):
        print("ID:", self.id)

    def show(self):
        print("Поле экземпляра базового класса")
        self.get()


class NewClass(BaseClass):
    def __init__(self, num, txt):
        super().__init__(num)
        self.name = txt

    def get(self):
        # super().get()
        BaseClass.get(self)
        print("Name:", self.name)


obj_base = BaseClass(1)
print("Вызываем метод show() из экземпляра obj_base:")
obj_base.show()

obj_new = NewClass(10, "Десятка")
print("Вызываем метод show() из экземпляра obj_new:")
obj_new.show()
