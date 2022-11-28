def how_many_times(a, b):
    if a == b:
        return b
    a, b = max(a,b), min(a,b)
    count = 0
    while b > 0:
        if a % b == 0:
            count += 1
        tmp = int(a/(int(a/b) + 1))
        b, a = tmp, a-(b-tmp)
    return count