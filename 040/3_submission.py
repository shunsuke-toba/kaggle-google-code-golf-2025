def p(g):
 t=g[0][0]==g[0][1];r=range(10)
 for y in r:
  for x in r:
   if g[y][x]==3:g[y][x]=(g[0][0],g[9*t][9*t^9])[(x,y)[t]>4]
 return g
