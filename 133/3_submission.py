def p(g):
 l=len;r=range;h=l(g);w=l(g[0]);o=[*map(list,g)]
 def f(y,x):
  c=[(y,x,g[y][x])];g[y][x]=0
  for Y,X in(1,0),(-1,0),(0,1),(0,-1):
   Y+=y;X+=x
   if h>Y>=0<=X<w and g[Y][X]:c+=f(Y,X)
  return c
 C=[f(y,x)for y in r(h)for x in r(w)if g[y][x]]
 B=()
 for c in C:
  d=[*zip(*c)][2]
  if l(c)>l(B)and 1 in map(d.count,d):B=c;p=min(d,key=d.count);Y,X=c[d.index(p)][:2]
 O=[(y-Y,x-X)for y,x,v in B if v^p]
 for c in C:
  if(A:=[(y,x)for y,x,v in c if v==p]):
   a,b=min(A);m=int(l(A)**.5);L=next(v for *_,v in c if v^p)
   for u,v in O:
    for i in r(m):o[a+u*m+i][b+v*m:b+v*m+m]=[L]*m
 return o

