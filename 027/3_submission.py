def p(g,o=4):
 for t in range(99):
  if g[r:=t//10][t%10]:b=g[t%10];o%=b[-r]+2;b[~r+o]=2-b[~r+o]
 return g