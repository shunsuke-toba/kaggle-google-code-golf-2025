def p(g):
 k=max(r[i]&r[i+1]&r[i+2]&p[i+1]for r,p in zip(g[1:],g)for i in range(18));i=-1
 for c in zip(*g):
  i+=1;y=bytes(c).rfind(k)+1
  for r in g[y:]*y:r[i]=max(c[y:])
 return g