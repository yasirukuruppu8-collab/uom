import math

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def smallest_multiple(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

print(smallest_multiple(20))