def p(g):
 k=max(r[i-1]&r[i]&r[i+1]&p[i]for r,p in zip(g[1:],g)for i in range(19));i=-1
 for c in zip(*g):
  i+=1;y=bytes(c).rfind(k)+1
  for r in g[y:]*y:r[i]=max(c[y:])
 return g