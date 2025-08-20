def p(g):
 h=len(g);w=len(g[0]);v=[[0]*w for _ in g]
 def f(y,x):
  v[y][x]=1;c=[(y,x)]
  for Y,X in(1,0),(-1,0),(0,1),(0,-1):
   Y+=y;X+=x
   if h>Y>=0<=X<w and g[Y][X]and not v[Y][X]:c+=f(Y,X)
  return c
 C=[f(y,x)for i in range(h*w)if g[y:=i//w][x:=i%w]>v[y][x]==0]
 m=0
 for c in C:
  for k in{*(d:=[g[y][x]for y,x in c])}:
   if d.count(k)<2 and len(c)>m:
    p=c[d.index(k)];O=[(y-p[0],x-p[1])for y,x in c if g[y][x]^k];K=k;m=len(c)
 if m<1:return g
 o=[*map(list,g)]
 for c in C:
  if(A:=[(y,x)for y,x in c if g[y][x]==K]):
   Y,X=zip(*A);a=min(Y);b=min(X);Y=max(Y)+1-a;X=max(X)+1-b;L=next((v for y,x in c if(v:=g[y][x])^K),0)
   for u,v in O:
    for y in range(s:=a+u*Y,s+Y):
     for x in range(t:=b+v*X,t+X):
      if h>y>=0<=x<w:o[y][x]=L
 return o
