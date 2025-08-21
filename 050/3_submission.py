def p(g):
 for _ in 0,1:
  for r in g:
   try:a=r.index(8);b=r.index(8,a+1);r[a+1:b]=[3]*(b+~a)
   except:0
  g=[*map(list,zip(*g))]
 return g
