def p(g):
 e=enumerate;u,v,w=zip(*((i,j,x)for i,r in e(g)for j,x in e(r)if x));a,b,c,d=u[0]+1,u[-1],min(v)+1,max(v);m=w[3]
 for r in g[a:b]:r[c]=r[d-1]=m
 g[a][c:d]=r[c:d]=[m]*(d-c);return g
