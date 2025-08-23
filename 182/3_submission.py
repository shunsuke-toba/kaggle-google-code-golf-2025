def p(g):
 r=range(25);m=r[:16];t=next([k for k in r if(v:=g[y+1+k//5][x+1+k%5])and(c:=v)]for y in m for x in m if g[y][x]&g[y][x+1]&g[y+1][x]>4)
 for y in m:
  for x in m:
   if[k for k in r if g[y+k//5][x+k%5]]==t:
    for k in t:g[y+k//5][x+k%5]=c
 return g
