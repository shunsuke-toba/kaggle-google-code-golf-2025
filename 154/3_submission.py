def p(g):
 for _ in[0]*4:
  for r in(g:=[*map(list,zip(*g[::-1]))]):
   if{0,5}<{*r}:j=r.index(2);r[j-3:j+4]=0,0,0,2,*r[:j][:-4:-1]
 return g