def p(g):
 r=range(10);x=[(g[b],a)for a in r for b in r if g[a][b]];k=9+(sum(b[-a]-b[~a]for b,a in x)>0)
 for b,a in x:b[k-a]=b[k-a]or 2
 return g