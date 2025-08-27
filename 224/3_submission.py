def p(g):
 e=enumerate;u,v,w=zip(*((i,j,x)for i,r in e(g)for j,x in e(r)if x));a,c=u[0]+1,min(v)+1;d,w=max(v),w[3]
 for r in g[a:u[-1]]:r[c]=r[d-1]=w
 g[a][c:d]=r[c:d]=[w]*(d-c);return g
