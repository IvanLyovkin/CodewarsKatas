# https://www.codewars.com//kata/617ae98d26537f000e04a863

from collections import deque

def to_mountain(mat):
    d = deque(sorted((x, i, j) for i, r in enumerate(mat) for j, x in enumerate(r)))
    while d:
        _, i, j = d.pop()
        v = mat[i][j]
        for a, b in ((0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)):
            try:
                if (x:=i+a) >= 0 and (y:=j+b) >= 0 and mat[x][y] < (z:=v - 1):
                    mat[x][y] = z
                    d.appendleft((0, x, y))
            except IndexError:
                pass
    return mat