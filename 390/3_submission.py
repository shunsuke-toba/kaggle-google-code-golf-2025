def p(g):
 for _ in[0]*4:
  for r in(g:=[*map(list,zip(*g[::-1]))]):
   if{0,5}<{*r}:j=r.index(2)-3;r[j:j+7]=r[j:j+7][::-1]
 return g