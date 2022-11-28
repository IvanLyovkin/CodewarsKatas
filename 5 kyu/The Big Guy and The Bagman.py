from itertools import *

def best_route(a,c):
    d = {k: dict(zip(a,b)) for k,b in zip(a,c)}
    x = [i for i in a if i != 'Notgnihsaw']
    m,r = 1e9,[]
    for p in permutations(x,len(x)):
        p = ['Notgnihsaw'] + [*p]+['Notgnihsaw']
        s = sum(d[i][j] for i,j in zip(p,p[1:]))
        if s < m:
            m,r = s,p
    return r[1:]