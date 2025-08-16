def p(g):
 h=len(g);w=len(g[0]);R=range
 for i,j in[(i,j)for i in R(h)for j in R(w)if g[i][j]==2]:
  for d,e in((1,0),(-1,0),(0,1),(0,-1)):
   r=i+d;c=j+e
   while h>r>-1<=c<w and g[r][c]==0:r+=d;c+=e
   if h>r>-1<=c<w and g[r][c]==8:
    a,b=i,j
    while(a,b)!=(r,c):a+=d;b+=e;g[a][b]=2
    for m in R(r-1,r+2):
     for n in R(c-1,c+2):
      if h>m>-1<=n<w:g[m][n]=8
    g[r][c]=2
 return g
