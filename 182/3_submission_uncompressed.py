def p(g):
 t=next([i-0*(c:=g[y+i//5+1][x+i%5+1])for i in range(25) if g[y+i//5+1][x+i%5+1]]for y in range(16) for x in range(16) if g[y][x+1]>4<g[y+1][x])
 for y in range(16):
  for x in range(16):
   if[i for i in range(25) if g[y+i//5][x+i%5]]==t:
    for i in t:g[y+i//5][x+i%5]=c
 return g