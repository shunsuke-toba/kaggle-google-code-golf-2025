def p(g):
 for r in g:r[1:]=[c-4*(c>7)for c in r[1:]]
 for i in range(4**8):
  x=i//135%15;y=i//9%15;a=i//3%3-1;b=i%3-1;t=g[x][y];u=g[(x+a)%15][(y+b)%15];g[x][y]=3if t>u>5else 8if 7<u==t*2else t
 return g
