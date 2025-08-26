def p(g):
 h=len(g);w=len(g[0])
 for k in range(h*w):
  if g[i:=k//w][j:=k%w]:
   s=[(i,j)];k=g[i][j]=0
   for x,y in s:
    for a,b in(x+1,y),(x-1,y),(x,y+1),(x,y-1):
     if h>a>-1<b<w>0<g[a][b]:g[a][b]=0;s+=(a,b),
    k+=(((x+1,y)in s)+((x-1,y)in s))*(((x,y+1)in s)+((x,y-1)in s))
   for x,y in s:g[x][y]=-~k*5%9
 return g
