def p(g):
 r=range(16);k=range(25)
 t=next([i-0*(c:=g[y+i//5+1][x+i%5+1])for i in k if g[y+i//5+1][x+i%5+1]]for y in r for x in r if g[y][x+1]>4<g[y+1][x])
 for y in r:
  for x in r:
   if[i for i in k if g[y+i//5][x+i%5]]==t:
    for i in t:g[y+i//5][x+i%5]=c
 return g