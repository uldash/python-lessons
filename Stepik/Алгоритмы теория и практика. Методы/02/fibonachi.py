import time


class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))


def fib_recursia(n):
    if n < 2:
        return 1
    else:
        return fib_recursia(n - 1) + fib_recursia(n - 2)


def fib_massiv(n, f):
    for i in range(2, n):
        f.append(f[i - 1] + f[i - 2])


'''
with Profiler() as p:
    for i in range(40):
        print(fib_recursia(i), end=' ')  #n=40 - 108.413sec
'''
f = [1, 1]
with Profiler() as p:
    fib_massiv(100, f)
print(*f)  #n=40 - 0.000sec
