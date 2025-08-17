def p(g,R=range):
 h=len(g)
 for y in R(1,h-1):
  for x in R(1,len(g[0])):
   c=g[y][x]
   if c and g[y][x-1]==c and g[y-1][x]==c==g[y+1][x]:g[y][x]=0
 return g
