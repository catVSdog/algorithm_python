"""
Fibonacci 斐波那契数列
数列类似于: 1  1  2  3  5  8 13  21

F(n) =
        0                  // n = 0
        1                 // n = 1
        F(n-1) + F(n-2)  // n > 1
"""


def function(n):
    """递归"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return function(n - 1) + function(n - 2)


def function_b(n):
    """备忘录"""

    def help(n, cache):
        if n not in cache:
            cache[n] = help(n - 1, cache) + help(n - 2, cache)
        return cache[n]

    cache = {}
    cache[0] = 0
    cache[1] = 1

    return help(n, cache)


def function_c(n):
    """备忘录"""
    cache = [None] * (n + 1)
    cache[0] = 0
    cache[1] = 1

    def help(n, cache):
        if cache[n] is None:
            cache[n] = help(n - 1, cache) + help(n - 2, cache)
        return cache[n]

    return help(n, cache)


def function_d(n):
    """动态规划"""
    temp = [None] * (n + 1)
    if n <= 1:
        return n
    else:
        temp[0] = 0
        temp[1] = 1
        for i in range(2, n + 1):
            temp[i] = temp[i - 1] + temp[i - 2]
        return temp[n]


if __name__ == '__main__':
    assert function(0) == 0
    assert function(1) == 1
    assert function(3) == 2
    assert function_d(5) == function(5)
