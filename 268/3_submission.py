def p(g):
 n=len(g);R=range;r=lambda:[*map(list,zip(*g[::-1]))]
 for k in R(4):
  (a,c),*_,(b,d)=[(k//n,k%n)for k in R(n*n)if g[k//n][k%n]]
  if g[a][c+2]<1:break
  g=r()
 while b:
  b-=1;h=g[b];s=b<=a;t=a+~b;h[c+1+s:d-s]=[4]*(d+~c-2*s)
  if s*(t<c+2):h[c+1-t]=4
  if s*(t<=n-d):h[d-1+t]=4
 while k-4:g=r();k+=1
 return g