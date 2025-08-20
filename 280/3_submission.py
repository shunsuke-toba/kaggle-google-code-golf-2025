def p(g):
 *h,=map(list,g);H=len(g);W=len(g[0])
 for i in range(H*W):
  y=i//W;x=i%W
  if h[y][x]-2:continue
  for a,b in(1,0),(0,1),(-1,0),(0,-1):
   if H>y+a>-1<x+b<W and h[y+a][x+b]<1:break
  k=0;Y=y-a;X=x-b
  while H>Y>-1<X<W and h[Y][X]==3:k+=1;Y-=a;X-=b
  while 1:
   g[y][x]=2
   for t in range(1,k+1):
    try:g[y+b*t][x+a*t]=g[y-b*t][x-a*t]=3
    except:0
   if not(H>(y:=y+a)>-1<(x:=x+b)<W and h[y][x]<1):break
 return g
