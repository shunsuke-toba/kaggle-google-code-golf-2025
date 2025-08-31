def p(g):
 k=max(r[i]&r[i+1]&r[i+2]&p[i+1]for r,p in zip(g[1:],g)for i in range(18));i=20
 while i:
  i-=1;y=20;c=0
  while y>0<(b:=g[y-1][i])^k:y-=1;c|=b
  for r in g[y:]*y:r[i]=c
 return g