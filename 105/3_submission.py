def p(g):
 E=enumerate;R=range;Y,X=zip(*[(i,j)for i,r in E(g)for j,v in E(r)if v]);a,b=min(Y),max(Y);c,d=min(X),max(X)
 for i in R(a,b+1):
  for j in c,d:g[i][j]=g[i][j]or 2
 for j in R(c,d+1):
  for i in a,b:g[i][j]=g[i][j]or 2
 for i in R(a+1,b):
  if 1<sum(g[i][c+1:d]):
   for j in R(c,d+1):g[i][j]=g[i][j]or 2
 for j in R(c+1,d):
  if 1<sum(r[j]%2 for r in g[a+1:b]):
   for i in R(a,b+1):g[i][j]=g[i][j]or 2
 return g
