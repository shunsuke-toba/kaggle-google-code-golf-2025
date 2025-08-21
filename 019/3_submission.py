def p(g):
 g=[r+r for _ in(0,1)for r in g];h=len(g);w=len(g[0])
 for k in range(h*w):
  if g[r:=k//w][c:=k%w]%8:
   for i in r-1,r+1:
    for j in c-1,c+1:
     if h>i>-1<j<w:g[i][j]=g[i][j]or 8
 return g
