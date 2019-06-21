# Алгоритм Евклида нахождения НОД
def nod(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return nod(a % b, b)
    if b >= a:
        return nod(a, b % a)


def main():
    a, b = map(int, input().split())
    print(nod(a, b))


if __name__ == "__main__":
    main()
