def p(g):
 for r in g:r[1:]=[4|c&2for c in r[1:]]
 for i in range(4**8):t=g[x:=i//135%15][y:=i//9%15];u=g[(x+i%9//3-1)%15][(y+i%3-1)%15];g[x][y]+=4*(u==t*2>7)-5*(t>u>5)
 return g