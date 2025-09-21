def p(g):
 i=6**6
 while i:i-=1;t=g[x:=i//135%15][y:=i//9%15];u=g[(x+i%9//3-1)%15][(y+i%3-1)%15];g[x][y]=(i>44630 and (y and 4|t&2 or t) or t+4*(u-t==4)-5*(t>u>5))
 return g