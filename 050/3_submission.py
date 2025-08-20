def p(g):
 for _ in g,g:
  for r in g:
   t=[i for i,x in enumerate(r)if x>7]
   if t[1:]:r[t[0]+1:t[1]]=[3]*(t[1]+~t[0])
  g=list(map(list,zip(*g)))
 return g