# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 14:03:33 2018

@author: user
"""

symbs = dict([["a", "первый"], ["b", "второй"]])
more_symbs = dict([["c", "третий"], ["d", "четвертый"]])
symbs.update(more_symbs)
print("Словарь:", symbs)
print("Количество ключей в словаре:", len(symbs))
print("Элемент с ключом 'c':", symbs.get("c", "нет такого ключа"))
del symbs["c"]
print("Элемент с ключом 'c':", symbs.get("c", "нет такого ключа"))
print("Наличие элемента с ключом 'c':", "c" in symbs)
print("Ключи словаря:", list(symbs.keys()))
print("Значения элементов словаря:", list(symbs.values()))
print("Содержимое словаря:", list(symbs.items()))
print("Удаляется элемент со значением:", symbs.pop("b"))
print("Словарь", symbs)
symbs.clear()
print("Словарь", symbs)


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


slovar = {1: "a", 2: "b"}
print(get_key(slovar, "a").__class__)
