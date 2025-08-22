def p(g,R=range):
 n=len(g);f=max(map(max,g))
 def d(o,r,c,t,m):
  for i in R(m):
   s=(t+1)*i;a=r-s+t;b=r+s;C=c-s+t;D=c+s-1
   for y in R(a,b):
    if-1<y<n:
     if-1<C<n:o[y][C]=f
     if-1<D<n:o[y][D]=f
   for x in R(C,D+1):
    if-1<x<n:
     if-1<a<n:o[a][x]=f
     if 0<b<n+1:o[b-1][x]=f
  return o
 for o in 0,1:
  for k in R(n):
   r,c=(k,0)if o else(0,k)
   for t in 1,2:
    for s in 2,3:
     if d([[0]*n for _ in g],r,c,t,s+1)==g:return d([[5]*n for _ in g],r,c,t,n)
