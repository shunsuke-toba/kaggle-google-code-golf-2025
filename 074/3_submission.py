def p(g):
 n=30
 for _ in[1]*9:
  for i in range(n):
   for j in range(n):
    if 31-i<n and g[31-i][j]!=9:g[i][j]=g[31-i][j]
    if 31-j<n and g[i][31-j]!=9:g[i][j]=g[i][31-j]
    if g[j][i]!=9:g[i][j]=g[j][i]
 return g