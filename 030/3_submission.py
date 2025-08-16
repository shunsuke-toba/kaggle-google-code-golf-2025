def p(g):
 t={};[t.setdefault(v,i)for i,r in enumerate(g)for v in set(r)if v];n=[[0]*len(g[0])for _ in g]
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v:n[i+t[1]-t[v]][j]=v
 return n
