"""
最大公因数
"""


def gcd(a, b):
    print(f"{a}----{b}")
    if b == 0:
        return a
    return gcd(b, a%b)

if __name__ == '__main__':
    print(gcd(12, 18))