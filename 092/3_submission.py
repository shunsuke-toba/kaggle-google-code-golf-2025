def p(g):
 for _ in 0,1:
  for r in g:
   if c:=sum(r)-sum({*r}):a=r.index(c);b=r.index(c,a+1)+1;r[a:b]=[c]*(b-a)
  g=[*map(list,zip(*g))]
 return g
