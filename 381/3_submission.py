def p(g):
 for r in g[1:9]:
  if 2in r:
   k=r.index(2)
   while 2in r[k+1:]:k+=1;r[k]=r[k]or 9
 return g
