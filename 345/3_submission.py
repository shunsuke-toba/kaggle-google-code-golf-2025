def p(g):
 for x in range(10):
  y=9
  if g[9][x]:
   while y:a=g[y-1][x]>4;y-=1-a;x+=a;g[y][x]=2
 return g