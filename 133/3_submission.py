def p(g):
 h=len(g);w=len(g[0]);o=[*map(list,g)]
 def f(y,x):
  c=[(y,x,g[y][x])];g[y][x]=0
  for Y,X in(1,0),(-1,0),(0,1),(0,-1):
   Y+=y;X+=x
   if h>Y>=0<=X<w and g[Y][X]:c+=f(Y,X)
  return c
 C=[f(y,x)for y in range(h)for x in range(w)if g[y][x]]
 B=[];P=0
 for c in C:
  d=[v for *_,v in c]
  for k in{*d}:
   if d.count(k)==1 and len(c)>len(B):B=c;P=k;y0,x0=B[d.index(k)][:2]
 O=[(y-y0,x-x0)for y,x,v in B if v^P]
 for c in C:
  if(A:=[(y,x)for y,x,v in c if v==P]):
   h,w=zip(*A);a=min(h);b=min(w);h=max(h)+1-a;w=max(w)+1-b;L=next(v for *_,v in c if v^P)
   for u,v in O:
    for i in range(h):o[a+u*h+i][b+v*w:b+v*w+w]=[L]*w
 return o
