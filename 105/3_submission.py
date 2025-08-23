def p(g):
 e=enumerate;p=[(i,j)for i,r in e(g)for j,v in e(r)if v];y,x=zip(*p);a,b=min(y),max(y);c,d=min(x),max(x)
 for i in range(a,b+1):
  for j in range(c,d+1):g[i][j]=g[i][j]or 2*(i in(a,b)or j in(c,d)or sum((c<x<d)*(y==i)+(a<y<b)*(x==j)for y,x in p)>1)
 return g
