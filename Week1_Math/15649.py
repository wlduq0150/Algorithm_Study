def print_seq_list(num_lst, result_lst, m):
    if (len(result_lst) == m):
        print(" ".join(result_lst))
        return

    for i in range(0, len(num_lst)):
        new_result_lst = result_lst + [str(num_lst[i])]
        new_num_lst = list(filter(lambda x: x != num_lst[i], num_lst))
        print_seq_list(new_num_lst, new_result_lst, m)

[n, m] = [int(i) for i in input().split()]
num_lst = [i for i in range(1, n+1)]
print_seq_list(num_lst, [], m)