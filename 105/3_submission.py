def p(g):
 E=enumerate;P=[(i,j)for i,r in E(g)for j,v in E(r)if v];Y,X=zip(*P);a,b=min(Y),max(Y);c,d=min(X),max(X)
 for i in range(a,b+1):
  for j in range(c,d+1):
   if i in(a,b)or j in(c,d)or 1<sum(c<j<d for y,j in P if y==i)or 1<sum(a<i<b for i,x in P if x==j):g[i][j]=g[i][j]or 2
 return g
