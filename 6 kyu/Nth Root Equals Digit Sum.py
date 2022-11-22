def nth_root_equals_digit_sum(num):
    res = []
    for i in range(1, 1000):
        if sum(int(c) for c in str(i ** num)) == i:
            res.append(i ** num)
    return res