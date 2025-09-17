def p(g):
 r=range;_=[(i,j)for i in r(len(g))for j in r(13)if g[i][j]];(a,*c,b),x=zip(*_);d=max(x)
 for i in r(a,b+1):
  for j in r(2,d+1):g[i][j]=g[i][j]or(i in(a,b)or j in(2,d)or sum((2<x<d)*(y==i)+(a<y<b)*(x==j)for y,x in _)>1)*2
 return g