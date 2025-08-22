def p(g,R=range):
 n=len(g);f=max(map(max,g))
 def d(r,c,t,m,b):
  o=[[b]*n for _ in g]
  for i in R(m):
   s=(t+1)*i;A=r-s+t;B=r+s;C=c-s+t;E=c+s
   for y in R(A,B):
    if-1<y<n:
     if-1<C<n:o[y][C]=f
     if 0<E<=n:o[y][E-1]=f
   for x in R(C,E):
    if-1<x<n:
     if-1<A<n:o[A][x]=f
     if 0<B<=n:o[B-1][x]=f
  return o
 for k in R(n):
  for r,c in(k,0),(0,k):
   for t in 1,2:
    for s in 2,3:
     if d(r,c,t,s+1,0)==g:return d(r,c,t,n,5)
