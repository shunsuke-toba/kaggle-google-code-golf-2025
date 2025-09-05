def p(g):
 for _ in[0]*4:
  for r in(g:=[*map(list,zip(*g[::-1]))]):
   if{0,5}<{*r}:j=r.index(2);r[j-3:j+4]=*r[j:j+4][::-1],0,0,0
 return g