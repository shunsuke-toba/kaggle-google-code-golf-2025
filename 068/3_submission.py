def p(g):
 a=sum(g,[]);b=[v for v in a if v and a.count(v)<2][0]
 y,x=divmod(a.index(b),10)
 r=[[0]*10 for _ in g]
 for R in r[y-1:y+2]:R[x-1:x+2]=2,2,2
 r[y][x]=b;return r
