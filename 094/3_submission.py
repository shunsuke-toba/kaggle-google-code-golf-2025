def p(g):
 for _ in 0,1:
  L=[r for r in range(15)if 1in g[r]]
  for r in L[2],L[-3]:g[r]=[c-c//8*2for c in g[r]]
  g=[*zip(*g)]
 return g
