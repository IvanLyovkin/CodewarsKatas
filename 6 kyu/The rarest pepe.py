def find_rarest_pepe(pepes):
    x = {}
    for i in set(pepes):
        j = pepes.count(i)
        if j in x:
            x[j] += [i]
        else:
            x[j] = [i]
    if min(x.keys()) < 5:
        d = x[min(x.keys())]
        return d[0] if len(d) == 1 else sorted(d)
    else:
        return 'No rare pepes!'