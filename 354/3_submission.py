def p(g):
 for r in g:
  while 5in r:a=r.index(5);b=(*r,0).index(0,a);r[a:b]=[max(g[0][a:b])]*(b-a)
 return g