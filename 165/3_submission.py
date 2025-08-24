def p(g):
 k=max(r[i]*(r[i]==r[i+1]==r[i+2]==p[i+1])for r,p in zip(g[1:],g)for i in range(18))
 for i in range(20):
  y=20;c=0
  while y and (b:=g[y-1][i])^k:y-=1;c|=b
  for r in g[y:]*c*y:r[i]=c
 return g
