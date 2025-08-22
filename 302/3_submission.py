def p(g):
 for y in range(1,12):
  for x in range(1,12):
   if g[y][x]<1<g[y][x-1]==g[y-1][x]:
    s=g[y][x:].index(5)
    for t in g[y:y+s]:t[x:x+s]=[s+5]*s
 return g