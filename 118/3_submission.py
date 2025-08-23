def p(g):
 h=len(g);w=len(g[0]);u=set();f=lambda y,x:((a:=g[y][x])==2)-2*(a<1 or (y,x)in u);R=range;t=2
 while 1:
  B=m=I=J=0
  for r in(3,2)[::t-1]:
   for k in R(h*w):
    i=k//w;j=k%w
    b=sum(f(a,j)for a in R(i-r,i+r+1)if-1<a<h)+sum(f(i,c)for c in R(j-r,j+r+1)if-1<c<w)-f(i,j)
    if(b,-r)>(B,-m):B,m,I,J=b,r,i,j
  if B<1:return g
  t=m
  for d in R(-t,t+1):
   for y,x in (I+d,J),(I,J+d):
    u|={(y,x)};g[y][x]+=3*(g[y][x]==5)
