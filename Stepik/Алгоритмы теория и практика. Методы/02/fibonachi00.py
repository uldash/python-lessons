'''
Дано целое число 1≤n≤40, необходимо вычислить n-е число 
Фибоначчи (напомним, что F0=0, F1=1 и Fn=Fn−1+Fn−2 при n≥2).

Sample Input:

3
Sample Output:

2
'''


def fib(n):
    a, b, c = 1, 1, 1
    for _ in range(2, n):
        c = a + b
        a, b = b, c
    return c


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()