def p(g):
 E=enumerate;R=range;t=[(i,j)for i,r in E(g)for j,v in E(r)if v==1];Y,X=zip(*t);a=min(Y);b=max(Y);c=min(X);d=max(X)
 for i in R(a,b+1):g[i][c]=2-g[i][c]%2;g[i][d]=2-g[i][d]%2
 for j in R(c,d+1):g[a][j]=2-g[a][j]%2;g[b][j]=2-g[b][j]%2
 for j in R(c+1,d):
  if 1<sum(g[i][j]for i in R(a+1,b)):
   for i in R(a,b+1):g[i][j]=2-g[i][j]%2
 for i in R(a+1,b):
  if 1<sum(g[i][j]==1 for j in R(c+1,d)):
   for j in R(c,d+1):g[i][j]=2-g[i][j]%2
 return g
