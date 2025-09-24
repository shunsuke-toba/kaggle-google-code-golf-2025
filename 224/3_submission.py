def p(g):
 e=enumerate;(u,*_,a),v,w=zip(*((i,b,c)for i,r in e(g)for b,c in e(r)if c));c=min(v)+1;v=max(v)
 for r in g[u+1:a]:r[c]=r[v-1]=k=w[3]
 g[u+1][c:v]=r[c:v]=[k]*(v-c);return g