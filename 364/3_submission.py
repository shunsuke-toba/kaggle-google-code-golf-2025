def p(g):
 h=len(g);w=len(g[0])
 for k in range(h*w):
  if g[i:=k//w][j:=k%w]:
   s=[(i,j)];m=t=g[i][j]=0
   for x,y in s:
    for a,b in(x+1,y),(x-1,y),(x,y+1),(x,y-1):
     if h>a>-1<b<w>0<g[a][b]:g[a][b]=0;s+=(a,b),
    a=(x+1,y)in s;a+=(x-1,y)in s;b=(x,y+1)in s;b+=(x,y-1)in s;m|=a+b>2;t+=a*b
   for x,y in s:g[x][y]=m*2 or t*5-4
 return g
