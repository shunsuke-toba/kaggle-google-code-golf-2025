def p(g):
 R=[];a=enumerate
 for i,r in a(g):
  for j,v in a(r):
   if v%3:R+=[(i,j)]
   if v>2:c,d=i-5,j-5
 a,b=map(min,zip(*R))
 for i,j in R[::-1]:g[i][j]=0;g[i+c-a][j+d-b]=2
 return g
