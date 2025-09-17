def p(g):
 for r in g[1:9]:
  k=0
  while 2in r[k:]:r[k]=r[k]or(2in r[:k])*9;k+=1
 return g