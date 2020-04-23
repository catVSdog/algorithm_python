"""
爬楼梯问题
"""
def function_a(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return function_a(n - 1) + function_a(n - 2)


def function_b(n):
    cache = [0] * (n + 1)

    def help(cache, n):
        if n not in cache:
            cache[n] = help(cache, n-1) + help(cache, n-2)
        return cache[n]

    cache[1] = 1
    cache[2] = 2
    return help(cache, n)


def function_c(n):
    cache = [0] * (n +2)


    if n<= 2:
        return n
    else:

        cache[1] = 1
        cache[2] = 2
        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]

def function_d(n):
    temp = {}
    temp[1] = 1
    temp[2] = 2

    if n > 2:
        for i in range(3, n+1):
            temp[i] = temp[i-2] + temp[i-1]
    return temp[n]
if __name__ == '__main__':
    print(function_d(0))
