def p(g):
 e=enumerate;u,v=zip(*[(i,j)for i,r in e(g)for j,x in e(r)if x]);a,b=min(u)+1,max(u);c,d=min(v)+1,max(v);m=max({*sum(g,[])}-{5})
 for r in g[a:b]:r[c]=r[d-1]=m
 g[a][c:d]=r[c:d]=[m]*(d-c);return g
