def find_sum(n):
    sum_num = 0
    for i in range(1, n+1):
        sum_num += i
    return sum_num


print(find_sum(5))
