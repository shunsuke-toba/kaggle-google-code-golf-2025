def p(g):
 R=[];c=d=9
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v==2:R+=[(i,j)]
   if v>2:c=min(c,i);d=min(d,j)
 a,b=map(min,zip(*R))
 for i,j in R[::-1]:g[i][j]=0;g[i+c+1-a][j+d+1-b]=2
 return g
