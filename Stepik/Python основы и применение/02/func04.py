#Отсортируем список по фамилиям

x = [("Guido", "van", "Rossum"), ("Haskell", "Curry"), ("john", "Backus")]
import operator as op
x.sort(key=op.itemgetter(-1))
print(x)