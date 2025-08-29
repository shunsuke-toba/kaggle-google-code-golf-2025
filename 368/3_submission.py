def p(g):
 r=range(10);a=[(i,j)for i in r for j in r if g[i][j]%5];x,y=a[0]
 for i in r:
  for j in r:
   for s,t in a*(g[i][j]==5):g[i+s-x][j+t-y]=g[s][t]
 return g