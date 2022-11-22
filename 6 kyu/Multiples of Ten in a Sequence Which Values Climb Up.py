def st(n):
    s1 = 3**n + 2**n + 1
    s2 = 4**n + 2**n + 1
    s3 = 6**n + 5**n + 4**n + s1
    return s3 - s2 - s1

def sf(n):
    return (st(n + 1)-(5*st(n)) - 4)//4

def find_mult10_SF(n):
    return sf(n*4 - 1)