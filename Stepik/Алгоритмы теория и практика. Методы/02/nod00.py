def nod(a, b):
    c = 1
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            c = i
    return c


def main():
    a, b = map(int, input().split())
    print(nod(a, b))


if __name__ == "__main__":
    main()