def p(g):
 s=[(u,n)for u in range(len(g))for n in range(13)if g[u][n]];(a,*u,b),x=zip(*s);f=max(x)
 for u in range(a,b+1):
  for n in range(2,f+1):g[u][n]=g[u][n]or(u in(a,b)or n in(2,f)or sum((2<x<f)*(u==d)+(a<d<b)*(n==x)for d,x in s)>1)*2
 return g