def p(g):
 h=len(g);w=len(g[0])
 for k in range(h*w):
  i=k//w;j=k%w
  if g[i][j]:
   s=[(i,j)];g[i][j]=0
   for x,y in s:
    for a,b in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
     if h>a>-1<b<w>0<g[a][b]:g[a][b]=0;s+=(a,b),
   m=t=0
   for x,y in s:
    a=(x+1,y)in s;b=(x-1,y)in s;c=(x,y+1)in s;d=(x,y-1)in s
    m|=a+b+c+d>2;t+=a+b==c+d==1
   n=m*2 or 1+5*(t>1)
   for x,y in s:g[x][y]=n
 return g
