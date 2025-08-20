def p(g):
 W=15
 for i in range(225):
  if g[i//W][i%W]==8>0<i%W:g[i//W][i%W]=4
 for i in range(5**7):
  x=i//135%W;y=i//9%W;a=i//3%3-1;b=i%3-1;t=g[x][y];u=g[(x+a)%W][(y+b)%W];g[x][y]=3if t>u>5else 8if 7<u==t*2else t
 return g
