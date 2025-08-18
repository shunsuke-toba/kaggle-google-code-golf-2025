def p(g):
 for _ in[0]*32:
  for r in g:
   for c in range(1,len(r)):r[c]+=r[c-1]==1>r[c]
  g=[*map(list,zip(*g[::-1]))]
 return g
