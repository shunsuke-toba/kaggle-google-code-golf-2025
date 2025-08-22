def p(g):
 for _ in[0]*96:
  if sum(g[-1])<1:g.pop()
  g=[*zip(*g[::-1])]
 return[[c and g[0][0]for c in r[1:-1]]for r in g[1:-1]]