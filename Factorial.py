"""
阶乘
n! = 1 * 2 * 3 * 4 * ... *  n-1 * n
反向看
n! = n * (n-1 * (n-2 * (n-3 * (....* (2 * (1)))))...)
"""


class Factorial:
    @classmethod
    def function_a(cls, n):
        if n == 1:
            return 1
        else:
            return n * cls.function_a(n - 1)

    @staticmethod
    def function_b(n):

        def help(n, cache):
            if n not in cache:
                cache[n] = help(n - 1, cache) * n
            return cache[n]

        cache = {}
        cache[1] = 1

        return help(n, cache)

    @staticmethod
    def function_c(n):
        cache = [None] * (n + 1)
        cache[1] = 1

        def help(n, cache):
            if cache[n] is None:
                cache[n] = help(n - 1, cache) * n
            return cache[n]

        return help(n, cache)


if __name__ == '__main__':
    f = Factorial()
    print(f.function_c(5))
