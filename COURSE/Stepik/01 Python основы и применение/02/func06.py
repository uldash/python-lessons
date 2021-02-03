from functools import partial
import operator as op

x = [("Guido", "van", "Rossum"), ("Haskell", "Curry"), ("john", "Backus")]

sort_by_last = partial(list.sort, key=op.itemgetter(-1))
print(x)
sort_by_last(x)
print(x)
