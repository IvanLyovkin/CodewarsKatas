# https://www.codewars.com//kata/57040e445a726387a1001cf7

def fusc(n):
    a, b = 0, 1
    while n > 0:
        if n & 1:
            a += b
        else:
            b += a
        n >>= 1
    return a