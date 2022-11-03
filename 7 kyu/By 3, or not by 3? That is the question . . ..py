def divisible_by_three(st): 
    while len(st) > 1:
        st = [int(x) for x in st]
        st = str(sum(st))
    if len(st) == 1:
        if st == '3' or st == '6' or st == '9':
            return True
        else:
            return False