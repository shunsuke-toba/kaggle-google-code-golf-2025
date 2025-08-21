def p(g):
 o=[[3]*10 for _ in g]
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v==2:x,y=i,j
   elif v and v-2:k=v
 b=k in g[x][y-1:y+2];a=b and y+(g[x][y-1]!=k) or x+(g[x-1][y]!=k)
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v==k:o[i][j]=o[b and i or 2*a-i-1][b and 2*a-j-1 or j]=k
 return o
