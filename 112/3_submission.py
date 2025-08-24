def p(g,e=enumerate):
 y=0
 while 3not in g[y]:y+=1
 X=g[y].index(3)*2+1;y=y*2+1
 for Y,r in e(g):
  for x,c in e(r):
   if c%3:r[X-x]=g[y-Y][x]=g[y-Y][X-x]=2
 return g
