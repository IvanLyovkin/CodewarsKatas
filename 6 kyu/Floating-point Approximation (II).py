import math
def interp(f, l, u, n):
    S = (u - l) / n
    return [math.floor(f(l+S*i) * 100) / 100 for i in range(n)]