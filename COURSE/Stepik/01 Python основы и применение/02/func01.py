x = input().split()
xs = (int(i) for i in x)


def even(x):
    return x % 2 == 0


evens = filter(even, xs)
print(evens)
for i in evens:
    print(i)
