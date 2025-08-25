def p(g):
 for r in g:r[1:]=[c%4+4for c in r[1:]]
 for i in range(4**8):t=g[x:=i//135%15][y:=i//9%15];u=g[(x+i//3%3-1)%15][(y+i%3-1)%15];g[x][y]=3*(t>u>5)+8*(7<u==t*2)or t
 return g