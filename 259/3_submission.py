def p(g):
 for _ in 0,1:
  while max(g[0])<2:g=g[1:]
  while max(g[-1])<2:g=g[:-1]
  g=[*zip(*g)]
 return[[c*(c>1)for c in r]for r in g]
