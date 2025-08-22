def p(g):
 n=len(g)
 for k in 1,2:
  r,c=divmod(next(i for i in range(n*n)if g[i//n][i%n]==k),n)
  while-1<r<n>c>-1:g[r][c]=k;r+=2*k-3;c+=2*k-3
 return g
