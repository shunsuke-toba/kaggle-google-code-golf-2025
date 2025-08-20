def p(g,R=range):
 for i in R(1,len(g)-1):
  for j in R(1,len(g[0])-1):
   if g[i][j]*all(g[i+u][j+v]==g[i-1][j-1]>0for u in(-1,0,1)for v in(-1,0,1)if u|v):return[[g[i][j]]]