import math

def is_prime(n):
    if (n == 1): return False

    sqrt = math.isqrt(n)
    for i in range(2, sqrt+1):
        if (n % i == 0):
            return False
    return True

cnt = int(input())
num_lst = [int(i) for i in input().split()]
prime_lst = list(filter(is_prime, num_lst))
print(len(prime_lst))