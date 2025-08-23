def p(g):
 for r,a in enumerate(g):
  for c in range(10):
   if a[c]==3 and(r<1or g[r-1][c]-3)and(c<1or a[c-1]-3):
    k=1
    while a[c+k]==3:k+=1
    for C in c-k,c+k:
     if g[r+k][C:C+1]==[3]:
      for R,C in((r-k,2*C-c),(r+2*k,2*c-C)):
       for i in range(k*k):
        x,y=R+i//k,C+i%k
        if 0<=x<10>y>=0:g[x][y]=8
 return g
