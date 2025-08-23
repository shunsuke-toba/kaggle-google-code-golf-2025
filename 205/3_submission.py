def p(g):
 R=range;h=len(g);w=len(g[0]);m=0
 for a in R(h):
  for b in R(a+1,h+1):
   for c in R(w):
    v=g[a][c]
    for d in R(c+1,w+1):
     t=(b-a)*(d-c)
     if t>m and sum(g[y][x]!=v for y in R(a,b) for x in R(c,d))<4:m=t;A,B,C,D,V=a,b,c,d,v
 g=[r[C:D]for r in g[A:B]]
 P=[(y,x,v)for y,r in enumerate(g)for x,v in enumerate(r)if v!=V]
 for y,x,v in P:
  for r in g:r[x]=v
  g[y]=[v]*(D-C)
 return g
