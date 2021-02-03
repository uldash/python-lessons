# Отсортируем список по фамилиям

import operator as op
x = [("Guido", "van", "Rossum"), ("Haskell", "Curry"), ("john", "Backus")]
x.sort(key=op.itemgetter(-1))
print(x)
