def p(g):
 for _ in g*4:
  for r in(g:=[*map(list,zip(*g[::-1]))]):
   if{0,5}<{*r}:j=r[3]<2;r[j:j+7]=r[j:j+7][::-1]
 return g