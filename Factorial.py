"""
阶乘
n! = 1 * 2 * 3 * 4 * ... *  n-1 * n
反向看
n! = n * (n-1 * (n-2 * (n-3 * (....* (2 * (1)))))...)
"""


def Factorial(n):
    print(f" {n} *  ")
    if n <= 1:
        return n
    else:
        return n * Factorial(n - 1)


if __name__ == '__main__':
    print(Factorial(5))
