def p(g):
 for r in g[1:9]:
  if 2in r:i=r.index(2);j=10-r[::-1].index(2);r[i:j]=[x or 9for x in r[i:j]]
 return g
