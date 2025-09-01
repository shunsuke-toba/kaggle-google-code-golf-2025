def p(g):
 e=enumerate;u,v,w=zip(*((a:=i,b,c)for i,r in e(g)for b,c in e(r)if c));u=u[0]+1;c=min(v)+1;v=max(v)
 for r in g[u:a]:r[c]=r[v-1]=k=w[3]
 g[u][c:v]=r[c:v]=[k]*(v-c);return g