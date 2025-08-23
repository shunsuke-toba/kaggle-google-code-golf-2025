def p(g):
 n=len({*g[4]})+1;r=range(m:=5*n);i=g[0][1]<1;j=g[1][0]<1;g=[[g[x//n][y//n]for y in r]for x in r]
 for s in-1,1:
  for t in-1,1:
   x=n*(i+s+1)+s//2;y=n*(j+t+1)+t//2
   while-1<x<m>y>-1<g[x][y]<1:g[x][y]=2;x+=s;y+=t
 return g

