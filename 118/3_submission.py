def p(g):
 h=len(g);w=len(g[0]);u=[[0]*w for _ in g];f=lambda y,x:(g[y][x]==2)-(g[y][x]%8<1)*10-100*u[y][x];m=5;R=range
 while 1:
  B=S=I=J=0
  for s in 7,5:
   if m>s:break
   r=s//2
   for k in R(h*w):
    i=k//w;j=k%w
    b=sum(f(a,j)for a in R(i-r,i+r+1)if-1<a<h)+sum(f(i,c)for c in R(j-r,j+r+1)if-1<c<w)-f(i,j)
    if(b,-s)>(B,-S):B,S,I,J=b,s,i,j
  if B<1:return g
  m=S;r=m//2
  for d in R(-r,r+1):
   for y,x in((I+d,J),(I,J+d)):
    if-1<y<h and-1<x<w:u[y][x]=1;g[y][x]+=3*(g[y][x]==5)
