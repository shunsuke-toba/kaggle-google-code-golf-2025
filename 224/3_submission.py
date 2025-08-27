def p(g):
 e=enumerate;u,v,w=zip(*((i,j,x)for i,r in e(g)for j,x in e(r)if x));a,c=u[0]+1,min(v)+1;d=max(v)
 for r in g[a:u[-1]]:r[c]=r[d-1]=w[3]
 g[a][c:d]=r[c:d]=[w[3]]*(d-c);return g