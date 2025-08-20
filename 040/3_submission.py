def p(g):
 a=g[0][0];t=a==g[0][1];b=g[9*t][9-9*t];r=range(10)
 for y in r:
  for x in r:
   if g[y][x]and 0<(x,y)[t]<9:g[y][x]=(a,b)[(x>4,y>4)[t]]
 return g
