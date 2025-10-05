def p(g):
 e=[(s,u)for s in range(len(g))for u in range(13)if g[s][u]];(a,*s,b),x=zip(*e);d=max(x)
 for s in range(a,b+1):
  for u in range(2,d+1):g[s][u]=g[s][u]or(s in(a,b)or u in(2,d)or sum((2<x<d)*(s==y)+(a<y<b)*(u==x)for y,x in e)>1)*2
 return g
