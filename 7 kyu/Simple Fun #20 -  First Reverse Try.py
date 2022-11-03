def first_reverse_try(arr):
    if len(arr) > 1:
        c = arr[0]
        arr[0] = arr[-1]
        arr[-1] = c
    return arr