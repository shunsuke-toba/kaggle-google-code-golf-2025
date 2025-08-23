def p(g):
 R=range;h,w=len(g),len(g[0]);d=1,0,-1,0,1;s=[]
 for y in R(h):
  for x in R(w):
   if g[y][x]>4:
    t=[(y,x)];g[y][x]=0
    for y,x in t:
     for k in R(4):
      Y=y+d[k];X=x+d[k+1]
      if-1<Y<h and-1<X<w and g[Y][X]>4:g[Y][X]=0;t+=[(Y,X)]
    a,b=map(min,zip(*t));s+=[[[y-a,x-b]for y,x in t]]
 while s:
  b=T=U=V=0
  for t in s:
   for Y in 1,2:
    for X in R(w):
     f=1
     for y,x in t:
      u=y+Y;v=x+X;f+=u<3
      if u>=h or v>=w or g[u][v]:f=0;break
     if f>b:b=f;T=t;U,V=Y,X
  for y,x in T:g[U+y][V+x]=1
  s.remove(T)
 return g
