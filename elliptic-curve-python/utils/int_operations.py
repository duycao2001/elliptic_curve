from math import gcd, sqrt


def is_prime(a):
    if a == 0 or a == 1:
        return False
    if a == 2 or a == 3:
        return True
    for i in range(2, int(sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True


def is_odd_prime(a):
    return is_prime(a) and a % 2 == 1


def is_coprime(a, b):
    return gcd(a, b) == 1


def to_base_2(a):
    # phân tích a về dạng a = q.2^s, với q lẻ
    q, s = a, 0
    while q % 2 == 0:
        q /= 2
        s += 1
    return q, s