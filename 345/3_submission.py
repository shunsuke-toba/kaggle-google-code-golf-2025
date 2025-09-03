def p(g):
 for x in range(9):
  y=9
  while y*g[y][x]:a=g[y-1][x]>4;x+=a;y-=1-a;g[y][x]=2
 return g