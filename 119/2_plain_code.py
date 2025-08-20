# -*- coding: utf-8 -*-
def p(g):
    c=0
    while g[6][0]!=2:
        g = [*map(list,zip(*g[::-1]))]
        c+=1
    
    f=0
    if not 8 in g[0]:
        g=g[::-1]
        f=1

    wall = g[0].count(2)
    start = g[0].index(8)
    for i in range(12):g[i][abs(start-i-wall)+wall]=max(3,g[i][abs(start-i-wall)+wall])

    if f:
        g=g[::-1]

    while c%4:
        g = [*map(list,zip(*g[::-1]))]
        c+=1
    
    return g