def p(g):
 for _ in[0]*4:
  while max(g[0])<2:g=g[1:]
  g=[*zip(*g[::-1])]
 return[[c*(c>1)for c in r]for r in g]
