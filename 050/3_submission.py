def p(g):
 for _ in g,g:
  for r in g:
   t=[i for i,x in enumerate(r)if x>7];a,b=t[0],t[1]
   if t[1:]:r[a+1:b]=[3]*(b+~a)
  g=list(map(list,zip(*g)))
 return g