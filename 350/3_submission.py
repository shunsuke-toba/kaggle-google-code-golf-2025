def p(g,L=len):
 for r in range(L(g)):
  for c in range(L(g[0])):
   if g[r][c]==1:
    for d,e in[(-1,0),(1,0),(0,-1),(0,1)]:
     n,m,p=r+d,c+e,[]
     while 0<=n<L(g)and 0<=m<L(g[0]):
      if g[n][m]==1:
       for i,j in p:g[i][j]=8
       break
      p+=[(n,m)];n+=d;m+=e
 return g