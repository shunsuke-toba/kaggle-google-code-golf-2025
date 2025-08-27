def p(g):
 a=bytes(sum(g,[]));y,x=divmod(a.find(1)+a.rfind(1)>>1,len(g[0]))
 for k in-1,0,1:g[y+k][x]=g[y][x+k]=3
 return g