def get_max_div(n, m):
    num = min(n, m)

    max_div = 1
    for i in range(2, num+1):
        if (n % i == 0 and m % i == 0):
            max_div = i

    return max_div

def get_min_mul(n, m, max_div):
    mul = 2
    
    max_mul_cnt = n * m // mul

    for i in range(1, max_mul_cnt+1):
        min_mul = max_div * i
        if (min_mul >= n and min_mul % n == 0 and min_mul >= m and min_mul % m == 0):
            return min_mul
        mul += 1

    return n * m

[n, m] = [int(i) for i in input().split()]
max_div = get_max_div(n, m)
min_mul = get_min_mul(n, m, max_div)
print(max_div)
print(min_mul)