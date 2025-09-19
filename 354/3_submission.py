def p(g):
 for r in g:
  while 5in r:a=r.index(5);r[a]=next(filter(int,r[a-1:a]+g[0][a:]))
 return g