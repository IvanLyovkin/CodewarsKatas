def pattern(n):
    k = ''
    for i in range(1, n + 1):
        for j in range(0, i):
            k += str(n - j)
        if i != n:
            k += '\n'
    return k