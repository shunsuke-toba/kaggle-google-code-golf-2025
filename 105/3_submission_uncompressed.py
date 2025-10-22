def p(d):
 m=[(u,n)for u in range(len(d))for n in range(13)if d[u][n]];(o,*u,f),p=zip(*m);r=max(p)
 for u in range(o,f+1):
  for n in range(2,r+1):d[u][n]=d[u][n]or(u in(o,f)or n in(2,r)or sum((2<p<r)*(u==d)+(o<d<f)*(n==p)for d,p in m)>1)*2
 return d