x = input().split()
xs = (int(i) for i in x)

even = lambda x: x % 2 == 0

evens = list(filter(even, xs))
print(evens)