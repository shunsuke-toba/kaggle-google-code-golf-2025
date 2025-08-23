def p(g):
 h=[*map(list,g)]
 for r,a in enumerate(h):
  for c in range(10):
   if a[c]==3>a[c-1]+h[r-1][c]:
    k=a[c:].index(0)
    for C in c-k,c+k:
     if h[r+k][C:C+1]==[3]:
      for R,C in((r-k,2*C-c),(r+2*k,2*c-C)):
       for i in range(k*k):x=R+i//k;y=C+i%k;0<=x<10>y>=0 and g[x].__setitem__(y,8)
 return g
