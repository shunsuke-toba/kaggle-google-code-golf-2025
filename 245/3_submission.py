def p(g):
 R=[];o=[[0]*len(r)for r in g];c=d=99
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v==2:R+=[(i,j)]
   if v>2:o[i][j]=3;c=min(c,i);d=min(d,j)
 a,b=map(min,zip(*R))
 for i,j in R:o[i-~c-a][j-~d-b]=2
 return o
