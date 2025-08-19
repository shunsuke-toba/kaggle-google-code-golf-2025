def p(g):
 R=range;Y=len(g);X=len(g[0]);s={(i//X,i%X)for i in R(Y*X)if g[i//X][i%X]>1}
 for i,j in s:
  if {(i+1,j),(i-1,j),(i,j+1),(i,j-1)}&s:
   for y in R(i-1,i+2):
    for x in R(j-1,j+2):
     if X>x>=0<=y<Y and g[y][x]<1:g[y][x]=3
 return g
