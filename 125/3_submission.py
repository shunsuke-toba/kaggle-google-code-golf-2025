def p(g):
 for i in range(225):
  if g[i//15][i%15]==8>0<i%15:g[i//15][i%15]=4
 for i in range(5**7):
  x=i//135%15;y=i//9%15;a=i//3%3-1;b=i%3-1;t=g[x][y];u=g[(x+a)%15][(y+b)%15];g[x][y]=3if t>u>5else 8if 7<u==t*2else t
 return g
