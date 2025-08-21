def p(g):
 *h,=map(list,g);H=len(g);W=len(g[0])
 for i in range(H*W):
  if h[y:=i//W][x:=i%W]-2:continue
  for a,b in(1,0),(0,1),(-1,0),(0,-1):
   if h[y+a][x+b]<1:break
  k=0;Y=y-a;X=x-b
  while H>Y>-1<X<W>2<h[Y][X]:k+=1;Y-=a;X-=b
  while 1:
   for t in range(-k,k+1):
    try:g[y+b*t][x+a*t]=3
    except:0
   g[y][x]=2
   if not(H>(y:=y+a)>-1<(x:=x+b)<W>1>h[y][x]):break
 return g
