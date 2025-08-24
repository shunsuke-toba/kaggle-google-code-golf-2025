def p(g,r=range):
 h=[*map(list,g)]
 for c in r(60):
  y,x=c//6,c%6;f=g[y][x+2]
  if f>1:
   for y in r(y-2-g[y-2][x],y+3-(y>7)):
    for X in r(x,x+5):h[y][X]=g[y][X]or f
 return h
