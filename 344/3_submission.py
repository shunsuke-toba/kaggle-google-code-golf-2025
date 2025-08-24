def p(g):
 for _ in 0,1:
  for r in g:r[:]=map(int,''.join(map(str,r)).replace('32','80').replace('23','08'))
  g=[*map(list,zip(*g))]
 return g