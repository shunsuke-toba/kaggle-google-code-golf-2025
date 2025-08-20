def p(g):
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v==2:
    for i in 1,-1:g[y+i][x+i]=g[y+i][x-i]=4
   if v==1:
    for i in 1,-1:g[y+i][x]=g[y][x+i]=7
 return g
