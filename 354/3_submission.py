def p(g):
 for r in g:
  while 5in r:a=r.index(5);r[a]=a and r[a-1]or next(filter(None,g[0][a:]))
 return g