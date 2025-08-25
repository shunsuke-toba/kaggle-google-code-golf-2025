E=enumerate
def p(g):
 for y,r in E(g):
  for x,v in E(r):
   if 0<v<3:w=v>1;g[y+1][x+w]=g[y-1][x-w]=g[y+w][x-1]=g[y-w][x+1]=7-3*w
 return g
