def p(g):
 n=len(g);r=lambda x:[*map(list,zip(*x[::-1]))]
 (a,c),*_,(b,d)=[(i//n,i%n)for i in range(n*n)if g[i//n][i%n]]
 if g[a][c+2]:return r(r(r(p(r(g)))))
 while b:
  b-=1;h=g[b];s=b<=a;t=a+~b;h[c+1+s:d-s]=[4]*(d+~c-2*s)
  if s*(t<c+2):h[c+1-t]=4
  if s*(t<=n-d):h[d-1+t]=4
 return g