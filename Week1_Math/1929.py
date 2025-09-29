import math

def get_between_prime_list(m, n):
    lst = [i if i >= m else 0 for i in range(0, n+1)]
    lst[1] = 0

    sqrt = math.isqrt(n)
    for i in range(2, sqrt+1):
        mul = 2
        while (i * mul <= n):
            lst[i * mul] = 0
            mul += 1
    
    return filter(lambda x: x != 0, lst)

[m, n] = [int(i) for i in input().split()]
prime_lst = get_between_prime_list(m, n)
for i in prime_lst:
    print(i)