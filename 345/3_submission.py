def p(g):
 for x,c in enumerate(g[9]):
  y=9
  while c*y:a=g[y-1][x]>4;y-=1-a;x+=a;g[y][x]=2
 return g