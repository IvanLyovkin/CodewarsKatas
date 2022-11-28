def look_and_say_and_sum(N):
    l=[1]
    for i in range(N-1):
        res = [1,l[0]]
        for i in range(1,len(l)):
            if l[i] == res[-1]:
                res[-2] += 1
            else:
                res += [1,l[i]] 
        l = res
    return sum(l)