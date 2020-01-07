"""
Fibonacci 斐波那契数列
数列类似于: 1  1  2  3  5  8 13  21

F(n) =
        0                  // n = 0
        1                 // n = 1
        F(n-1) + F(n-2)  // n > 1
"""


def function(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return function(n - 1) + function(n - 2)


if __name__ == '__main__':
    assert function(0) == 0
    assert function(1) == 1
    assert function(3) == 2
    assert function(5) == 5
