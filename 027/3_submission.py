def p(g,o=2):
 for t in range(99):
  if g[r:=t//10][c:=t%10]:b=g[c];o=(b[-r],o)[o<2];b[~r+o]=2-b[~r+o]
 return g