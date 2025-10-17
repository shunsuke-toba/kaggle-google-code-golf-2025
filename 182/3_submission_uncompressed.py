def p(g):
 i=next([f-0*(n:=g[e+f//5+1][r+f%5+1])for f in range(25) if g[e+f//5+1][r+f%5+1]]for e in range(0x10) for r in range(0x10) if g[e][r+1]>4<g[e+1][r])
 for e in range(0x10):
  for r in range(0x10):
   if i==[f for f in range(25) if g[e+f//5][r+f%5]]:
    for f in i:g[e+f//5][r+f%5]=n
 return g