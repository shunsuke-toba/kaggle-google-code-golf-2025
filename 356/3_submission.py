def p(g):
 for _ in g,g:
  for r in g:
   t=[i for i,x in enumerate(r)if x==8]
   for a,b in zip(t,t[1:]):r[a+1:b]=[9]*(b+~a)
  g=list(map(list,zip(*g)))
 return[[x&8for x in r]for r in g]