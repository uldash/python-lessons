x = [("Guido", "van", "Rossum"), ("Haskell", "Curry"), ("john", "Backus")]
import operator as op
from functools import partial

sort_by_last = partial(list.sort, key=op.itemgetter(-1))
print(x)
sort_by_last(x)
print(x)