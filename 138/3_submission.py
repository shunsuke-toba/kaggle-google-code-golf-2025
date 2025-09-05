def p(g):
 for i in range(8):
  while 0in g[0]:g=g[1:]
  if i&4:g=[[(c,r[0])[r[0]in r[j:]]for j,c in enumerate(r)]for r in g]
  g=[*zip(*g)][::-1]
 return g