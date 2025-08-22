def p(g):
 h=len(g);w=len(g[0]);o=[*map(list,g)]
 def f(y,x):
  c=[(y,x,g[y][x])];g[y][x]=0
  for Y,X in(1,0),(-1,0),(0,1),(0,-1):
   Y+=y;X+=x
   if h>Y>=0<=X<w and g[Y][X]:c+=f(Y,X)
  return c
 C=[f(y,x)for i in range(h*w)if g[y:=i//w][x:=i%w]]
 B=[];K=0
 for c in C:
  d=[v for _,_,v in c]
  for k in{*d}:
   if d.count(k)==1 and len(c)>len(B):B=c;K=k;p0=B[d.index(k)][:2]
 O=[(y-p0[0],x-p0[1])for y,x,v in B if v!=K]
 for c in C:
  if(A:=[(y,x)for y,x,v in c if v==K]):
   Y,X=zip(*A);a=min(Y);b=min(X);Y=max(Y)+1-a;X=max(X)+1-b;L=next(v for y,x,v in c if v^K)
   for u,v in O:
    for y in range(s:=a+u*Y,s+Y):
     for x in range(t:=b+v*X,t+X):o[y][x]=L
 return o
