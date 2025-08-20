def p(g):
 a=[r[:]for r in g];h=len(g);w=len(g[0])
 for y,r in enumerate(a):
  for x,v in enumerate(r):
   if v>1:
    X=range(max(0,x-2),min(w,x+3))
    for i in range(max(0,y-2),min(h,y+3)):
     for j in X:
      if g[i][j]<1:g[i][j]=v
    u=y-2
    if u>=0 and any(a[u][j]==1 for j in X):
     u-=1
     if u>=0:
      for j in X:
       if g[u][j]<1:g[u][j]=v
 return g
