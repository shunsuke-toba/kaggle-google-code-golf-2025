def p(g):
 t=next([i-0*(c:=g[y+i//5+1][x+i%5+1])for i in range(25) if g[y+i//5+1][x+i%5+1]]for y in range(0x10) for x in range(0x10) if g[y][x+1]>4<g[y+1][x])
 for y in range(0x10):
  for x in range(0x10):
   if t==[i for i in range(25) if g[y+i//5][x+i%5]]:
    for i in t:g[y+i//5][x+i%5]=c
 return g