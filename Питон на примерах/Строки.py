# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 14:48:42 2018

@author: user
"""

str1="aaaaaaa \
dddddd"
print(str1)
str2="""aaaaaaa
dddddd"""
print(str2)

txt="Мы изучаем язык PYTHON"
print(txt)
print(txt.upper())
print(txt.lower())
print(txt.capitalize())
print(txt.title())
print(txt.swapcase())

txt="""И.В. Гете. "Фауст" (отрывок):
    Бессодержательную речь
    Всегда легко в слова облечь.
    Из голых слов, ярясь и споря,
    Возводят здания теорий.
    Словами вера лишь жива.
    Как можно отрицать слова?"""
print(txt)
word="слов"
print("Подстрока встречается",txt.count(word),"раза")
print("Первая позиция:",txt.index(word))
print("Следующая позиция:",txt.find(word,txt.index(word)+1))
print("Последняя позиция:",txt.rindex(word))
print("В начале инициалы?:",txt.startswith("И.В. "))
print("В конце знак вопроса?:",txt.endswith("?"))
print("\n",txt.replace(" ","_"))
print()
print("Словами вера лишь жива___".strip("_"))
