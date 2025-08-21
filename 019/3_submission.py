def p(g):
 g=[r*2 for _ in(0,1)for r in g]
 h=len(g);w=len(g[0])
 for k in range(h*w):
  if g[r:=k//w][c:=k%w]%8:
   for i in r-1,r+1:
    for j in c-1,c+1:
     if h>i>-1<w>j>-1 and g[i][j]<1:g[i][j]=8
 return g
