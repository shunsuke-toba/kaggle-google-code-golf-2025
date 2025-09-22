def p(g):
 for i in range(6**6):t,u=g[x:=i//135%15][y:=i//9%15],g[(x+i%9//3-1)%15][(y+i%3-1)%15];g[x][y]=(t+4*(u-t==4)-5*(t>u>5),y and t&6|4 or t)[i<2025]
 return g