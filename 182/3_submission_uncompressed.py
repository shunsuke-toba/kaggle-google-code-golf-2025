def p(g):
 r=range(25)
 t=next([k-0*(c:=v)for k in r if(v:=g[y+k//5+1][x+k%5+1])]for y in r[:16] for x in r[:16] if g[y][x+1]>4<g[y+1][x])
 for y in r[:16]:
  for x in r[:16]:
   if[k for k in r if g[y+k//5][x+k%5]]==t:
    for k in t:g[y+k//5][x+k%5]=c
 return g