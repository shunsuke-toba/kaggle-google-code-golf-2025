def p(g):
 n=len({*g[4]})+1
 for m in range(4):
  i,j=m>>1,m&1
  if g[i][j]==g[i+1][j]==g[i][j+1]==g[i+1][j+1]>0:
   r=range(5*n);g=[[g[x//n][y//n]for y in r]for x in r]
   for s in-1,1:
    for t in-1,1:
     x=n*(i+s+1)-(s<0);y=n*(j+t+1)-(t<0)
     while-1<x<5*n>y>-1<g[x][y]<1:g[x][y]=2;x+=s;y+=t
   return g
