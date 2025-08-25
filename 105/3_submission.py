def p(g):
 e=enumerate;r=range;p=[(i,j)for i,u in e(g)for j,v in e(u)if v];y,x=zip(*p);a,b=y[0],y[-1];d=max(x)
 for i in r(a,b+1):
  for j in r(2,d+1):g[i][j]=g[i][j]or 2*(i in(a,b)or j%d<3 or sum((2<x<d)*(y==i)+(a<y<b)*(x==j)for y,x in p)>1)
 return g
