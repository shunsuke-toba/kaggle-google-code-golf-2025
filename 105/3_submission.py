def p(g):
 E=enumerate;R=range;Y,X=zip(*[(i,j)for i,r in E(g)for j,v in E(r)if v]);a,b=min(Y),max(Y);c,d=min(X),max(X);I=R(a,b+1);J=R(c,d+1)
 for i in I:
  for j in c,d:g[i][j]=2-g[i][j]%2
 for j in J:
  for i in a,b:g[i][j]=2-g[i][j]%2
 for i in R(a+1,b):
  if 1<sum(g[i][c+1:d]):
   for j in J:g[i][j]=2-g[i][j]%2
 for j in R(c+1,d):
  if 1<sum(r[j]&1 for r in g[a+1:b]):
   for i in I:g[i][j]=2-g[i][j]%2
 return g
