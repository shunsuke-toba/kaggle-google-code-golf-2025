def p(g):
 for r in g[1:9]:
  k=p=0
  while 2in r[k:]:p=r[k]=r[k]or(p>1)*9;k+=1
 return g