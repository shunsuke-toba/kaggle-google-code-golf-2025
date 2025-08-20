def p(g):
 for j in 1,3,5,7:
  for r in g[(2-sum([*zip(*g)][j]))//4:]:r[j]=8
 return g