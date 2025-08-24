def p(g):
 r=range(1,12)
 for y in r:
  for x in r:
   if g[y][x]<1<g[y][x-1]*g[y-1][x]:
    for t in g[y:y+(s:=g[y][x:].index(5))]:t[x:x+s]=[s+5]*s
 return g