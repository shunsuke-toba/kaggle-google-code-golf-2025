def p(g):
 n=len(g);(a,c),*_,(b,d)=[(i//n,i%n)for i in range(n*n)if g[i//n][i%n]]
 if g[a][c+2]:return[*zip(*p([*zip(*g)][::-1])[::-1])]
 while b:
  b-=1;h=g[b]=[*g[b]];s=b<=a;h[c-~s:d-s]=[4]*(d+~c-2*s)
  for k in c+b-a+2,d-2-b+a:
   if s>0<=k<n:h[k]=4
 return g