def bulk(arr):
    arr = [i.split(', ') for i in arr]
    p, c = 0, 0
    for i in arr:
        for j in i:
            arr, b = int(j.split()[0][:-1]), j.split()[1]
            p += (arr*food[b][0]/100)
            c += (arr*((food[b][0]+food[b][1])*4 + 9*food[b][2])/100)
    p, c = p*100/100,c*100/100
    p, c = int(p) if int(p)==p else p, int(c) if int(c)==c else c
    return 'Total proteins: {} grams, Total calories: {}'.format(p,c)