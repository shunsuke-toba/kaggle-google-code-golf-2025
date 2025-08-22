def p(g):
 H=len(g);W=len(g[0])
 P=[(y,x)for y in range(H)for x in range(W)if g[y][x]==2]
 for y,x in P:
  for a,b in(1,0),(0,1),(-1,0),(0,-1):
   if g[y+a][x+b]<1:break
  k=0;Y=y-a;X=x-b
  while H>Y>-1<X<W>2<g[Y][X]:k+=1;Y-=a;X-=b
  while H>y>-1<x<W:
   for t in range(-k,k+1):g[y+b*t][x+a*t]=3
   g[y][x]=2
   y+=a;x+=b
 return g
