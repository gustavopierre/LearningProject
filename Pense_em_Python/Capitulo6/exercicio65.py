def gcd(a, b):
    if b == 0:
        return a
    else:
        a, b = b, a % b
        return gcd(a, b)


print(gcd(51, 7))
