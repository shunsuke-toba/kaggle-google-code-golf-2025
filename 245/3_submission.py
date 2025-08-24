def p(g):
 R=[];f=2
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v==2:R+=[(i,j)]
   elif v>f:c,d=i,j;f=v
 a,b=map(min,zip(*R))
 for i,j in R[::-1]:g[i][j]=0;g[i+c+1-a][j+d+1-b]=2
 return g
