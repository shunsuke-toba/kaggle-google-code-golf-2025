def p(g):
 for _ in g,g:
  for r in g:
   a=9
   for i in range(10):
    if r[i]==8:r[a+1:i]=[9]*(i+~a);a=i
  g=[*map(list,zip(*g))]
 return[[x&8 for x in r]for r in g]