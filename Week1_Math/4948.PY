import math

num_lst = []

while True:
    num = int(input())

    if (num == 0):
        break

    num_lst.append(num)

max_n = max(num_lst)
max_m = max_n * 2

prime_lst = [i for i in range(0, max_m+1)]
prime_lst[1] = 0

sqrt = math.isqrt(max_m)
for i in range(2, sqrt+1):
    mul = 2
    while (i * mul <= max_m):
        prime_lst[i * mul] = 0
        mul += 1


for num in num_lst:
    sliced_lst = list(filter(lambda x: x != 0, prime_lst[num+1:(num*2+1)]))
    print(len(sliced_lst))