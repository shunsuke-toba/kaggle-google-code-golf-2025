def p(g):
 r=range(9)
 for y in r:
  for x in r:
   if(c:=g[y][x])==g[y+1][x+1]>0:
    i,j=y,x
    while-1<i<10>-1<j<10:g[i][j]=c;i+=c*2-3;j+=c*2-3
 return g
