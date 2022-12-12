# https://www.codewars.com//kata/58aa8b0538cf2eced5000115

def exchange_sort(sequence):
    x = 0
    y = 0
    for f, g in zip(sequence, sorted(sequence)):
        if f < g:
            x += 1
        elif f > g:
            y += 1
    return max(x, y)