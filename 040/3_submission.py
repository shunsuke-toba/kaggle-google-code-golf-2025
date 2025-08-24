def p(g):
 for y in (r:=range(10)):
  for x in r:
   if g[y][x]==3:g[y][x]=(g[0][0],g[9][9])[(x,y)[g[0][0]!=g[9][0]]>4]
 return g

