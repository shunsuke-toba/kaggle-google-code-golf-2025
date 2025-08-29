def p(g):
 for r in g[1:9]:
  k=(r+[2]).index(2)
  while 2in r[k:]:r[k]=r[k]or 9;k+=1
 return g