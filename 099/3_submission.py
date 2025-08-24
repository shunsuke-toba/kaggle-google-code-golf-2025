def p(g,r=range):
 h=g;g=[*map(list,g)]
 for c in r(60):
  y,x=c//6,c%6;f=h[y][x+2]
  if f>1:
   for y in r(y-2-h[y-2][x],min(y+3,10)):
    for X in r(x,x+5):
     if h[y][X]^1:g[y][X]=f
 return g
