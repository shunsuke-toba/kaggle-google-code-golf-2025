def p(g):
 H=len(g);W=len(g[0])
 for y,x in[(y,x)for y in range(H)for x in range(W)if g[y][x]==2]:
  for a,b in(1,0),(0,1),(-1,0),(0,-1):
   if g[y+a][x+b]<1:break
  Y=y-a;X=x-b;k=0
  while H>Y>-1<X<W>2<g[Y][X]:k+=1;Y-=a;X-=b
  while H>y>-1<x<W:
   for t in range(-k,k+1):g[y+b*t][x+a*t]=3
   g[y][x]=2;y+=a;x+=b
 return g
