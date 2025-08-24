def p(g):
 R=[]
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v==2:R+=[(i,j)]
   elif v==3:c,d=i,j
 a,b=map(min,zip(*R))
 for i,j in R[::-1]:g[i][j]=0;g[i+c-5-a][j+d-5-b]=2
 return g
