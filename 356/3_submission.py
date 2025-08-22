def p(g):
 for _ in g,g:
  for r in g:
   for a,b in zip(t:=[i for i,x in enumerate(r)if x==8],t[1:]):r[a+1:b]=[9]*(b+~a)
  g=[*map(list,zip(*g))]
 return[[x&8 for x in r]for r in g]