def p(g):
 for _ in g,g:
  g=[*map(list,zip(*g))]
  for r in g:
   try:a=r.index(8)+1;b=r.index(8,a);r[a:b]=[3]*(b-a)
   except:0
 return g
