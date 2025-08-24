def p(g):
 k=[r[i]for r,p in zip(g[1:],g)for i in range(18)if r[i]==r[i+1]==r[i+2]==p[i+1]>0][0]
 for x in range(20):
  y=20;c=0
  while y and (b:=g[y-1][x])^k:y-=1;c|=b
  for t in g[y:]*c*y:t[x]=c
 return g

