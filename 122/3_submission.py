def p(g):
 for y,r in enumerate(g):
  if 2 in r:break
 x=r.index(2)
 d=3in g[y+1][x+3:x+4]
 for r in g[y:y+3]:r[x:x+3]=0,0,0
 X,Y=x+2*d,y+2-2*d
 for r in g[Y:Y+3]:r[X:X+3]=2,2,2
 g[y+1][x+1]=g[Y+1][X+1]=3
 return g
