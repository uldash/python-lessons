'''
Даны целые числа 1≤n≤1018 и 2≤m≤105, необходимо найти остаток от деления n-го числа Фибоначчи на m.
Период Пезано
https://way23.ru/%D0%BF%D0%BE%D0%B8%D1%81%D0%BA-%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4%D0%B0-%D0%BF%D0%B8%D0%B7%D0%B0%D0%BD%D0%BE/
'''


def fib(n, m):
    def find_pisano(n, m):
        pisano = []
        pisano.append(0)

        # при делении на 1 остаток будет всегда 0
        if m == 1:
            return pisano

        pisano.append(1)

        # при m > 0 остатки от деления первого и второго числа Фибоначчи
        # всегда 0 и 1
        if n <= 1:
            return pisano

        n0 = 0
        n1 = 1
        for __ in range(m * 6):
            # для ускорения вычисляем полностью числа Фибоначчи
            # берём только остатки по модулю m
            n0, n1 = n1, (n0 + n1) % m
            pisano.append(n1 % m)

            # Проверяем не начался ли новый период
            # период всегда начинается с 0 и 1
            if pisano[len(pisano) - 1] == 1 and pisano[len(pisano) - 2] == 0:
                break

        return pisano[:-2]

    pisano = find_pisano(n, m)
    #print(pisano)
    #print(pisano[n % len(pisano)])
    return pisano[n % len(pisano)]


def main():
    n, m = map(int, input().split())
    print(fib(n, m))


if __name__ == "__main__":
    main()