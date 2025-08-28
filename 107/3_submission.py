def p(g):
 n=len({*g[4]})+1;r=range(5*n);g=[[g[x//n][y//n]for y in r]for x in r]
 for s in-1,1:
  for t in-1,1:
   x=n*(s-~(g[0][n]<1))+s//2;y=n*(t-~(g[n][0]<1))+t//2
   while g[x][y]<1:g[x][y]=2;x+=s;y+=t
 return g