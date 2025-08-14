def p(g):
 n=len(g);m=n*n
 for b in range(m*96):
  r,c=b%m//n,b%m%n
  if c>0and g[r][c-1]==1and g[r][c]==0:g[r][c]=1
  if b%m==0:g=[list(row)for row in zip(*g[::-1])]
 return g