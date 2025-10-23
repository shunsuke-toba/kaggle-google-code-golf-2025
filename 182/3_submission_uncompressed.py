def p(g):
 i=next([f-0*(n:=g[e+f//5][r+f%5])for f in range(25) if g[e+f//5][r+f%5]]for e in range(16)[1:]for r in range(16)[1:] if g[e-1][r]==g[e][r-1]==5)
 for e in range(16):
  for r in range(16):
   if i==[f for f in range(25) if g[e+f//5][r+f%5]]:
    for f in i:g[e+f//5][r+f%5]=n
 return g