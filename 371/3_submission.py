def p(g,A=enumerate):
 y,x=zip(*((i,j)for i,r in A(g)for j,v in A(r)if v))
 y=sum(y)>>1;x=sum(x)>>1
 for k in-1,0,1:g[y+k][x]=g[y][x+k]=3
 return g
