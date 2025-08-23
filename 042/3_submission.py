def p(g):
 h=[*map(list,g)]
 for r,a in enumerate(h):
  for c in range(10):
   if a[c]==3>a[c-1]|h[r-1][c]:
    k=a[c:].index(0)
    for d in-1,1:
     if h[r+k][c+d*k]>2:
      for s,t in(-k,2*d*k),(2*k,-d*k):
       for i in range(k*k):x=r+s+i//k;y=c+t+i%k;0<=x<10>y>=0 and g[x].__setitem__(y,8)
 return g
