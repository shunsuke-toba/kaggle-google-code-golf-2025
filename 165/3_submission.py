def p(g):
 k=max(r[i]&r[i+1]&r[i+2]&p[i+1]for r,p in zip(g[1:],g)for i in range(18))
 i=0
 for c in zip(*g):
  y=bytes(c).rfind(k)+1;v=max(c[y:])
  for r in g[y:]*y:r[i]=v
  i+=1
 return g