# https://www.codewars.com//kata/57cebf1472f98327760003cd

def count_col_triang(ps):
    hs,ts = {},{}
    for [x,y],c in ps:
        if c not in hs:
            hs[c],ts[c] = [],0
        hs[c].append((x,y))
    for c in hs:
        cps = hs[c]
        for i in range(len(cps)-2):
            for j in range(i+1,len(cps)-1):
                for k in range(j+1,len(cps)):
                    if is_triangle(*cps[i],*cps[j],*cps[k]):
                        ts[c] += 1
    m = max(ts[c] for c in ts)
    p = [] if m==0 else [*sorted(c for c in ts if ts[c]==m),m]
    return [len(ps),len(hs),sum(ts[c] for c in ts),p]
                    
def is_triangle(x1,y1,x2,y2,x3,y3):
    a = (x1*(y2-y3) +
         x2*(y3-y1) +
         x3*(y1-y2))
    return a != 0