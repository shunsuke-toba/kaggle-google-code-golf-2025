def p(g):
 E=enumerate;R=range;P=[(i,j)for i,r in E(g)for j,v in E(r)if v];Y,X=zip(*P);a,b=min(Y),max(Y);c,d=min(X),max(X);I=R(a,b+1);J=R(c,d+1);S={i for i in R(a+1,b)if 1<sum(c<j<d for y,j in P if y==i)};T={j for j in R(c+1,d)if 1<sum(a<i<b for i,x in P if x==j)}
 for i in I:
  for j in J:
   if i in(a,b)or j in(c,d)or i in S or j in T:g[i][j]=g[i][j]or 2
 return g
