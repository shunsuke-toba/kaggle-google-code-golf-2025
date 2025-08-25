def p(g):
 r=range(10);x=[(a,b)for a in r for b in r if g[a][b]];k=9+(sum(g[b][-a]-g[b][~a]for a,b in x)>0)
 for a,b in x:g[b][k-a]=g[b][k-a]or 2
 return g
