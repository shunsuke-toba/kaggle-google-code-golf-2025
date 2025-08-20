def p(g,R=range):
 n=len(g)
 r,c=next((i,j)for i in R(n-1)for j in R(n-1)if g[i][j]==g[i][j+1]==g[i+1][j]==g[i+1][j+1]==3)
 for x in (c,c+1):
  for k in R(r-1,-1,-1):
   v=g[k][x]
   if v*(v-3):
    for t in R(k,r):g[t][x]=v
    break
  for k in R(r+2,n):
   v=g[k][x]
   if v*(v-3):
    for t in R(r+2,k+1):g[t][x]=v
    break
 for y in (r,r+1):
  for k in R(c-1,-1,-1):
   v=g[y][k]
   if v*(v-3):
    for t in R(k,c):g[y][t]=v
    break
  for k in R(c+2,n):
   v=g[y][k]
   if v*(v-3):
    for t in R(c+2,k+1):g[y][t]=v
    break
 return g