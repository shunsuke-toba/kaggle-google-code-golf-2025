def p(g):
 h=len(g);w=len(g[0]);r=[[0]*w for _ in g];F=sum(g,[])
 for i in(1,2):
  y,x=divmod(F.index(i),w);r[y][x]=i;t=11-4*i
  for Y,X in(1,0),(-1,0),(0,1),(0,-1):
   a,b=y+Y,x+X
   while h>a>=0<=b<w:
    if g[a][b]==t:r[y+Y][x+X]=t;break
    a+=Y;b+=X
 return r
