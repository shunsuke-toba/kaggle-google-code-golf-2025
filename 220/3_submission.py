def p(g):
 h,w=len(g),len(g[0])
 for y,x,c in [(i,j,c)for i in range(h)for j in range(w)if(c:=g[i][j])]:
  v=[c*2%10,c//2][~c&1]
  for k in range(9):
   i=y+k//3-1;j=x+k%3-1
   if h>i>=0<=j<w:g[i][j]=v
  g[y][x]=c
 return g
