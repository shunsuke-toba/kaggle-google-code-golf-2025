def p(g):
 for r in g:
  while 5 in r:a=r.index(5);c=(r[a:]+[0]).index(0);r[a:a+c]=[max(g[0][a:a+c])]*c
 return g
