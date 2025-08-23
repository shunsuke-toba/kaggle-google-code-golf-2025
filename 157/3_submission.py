def p(g):
 R=range;D=1,0,-1,0,1;s=[]
 for y in R(10):
  for x in R(15):
   if g[y][x]>4:
    t=[(y,x)];g[y][x]=0
    for y,x in t:
     for k in R(4):
      Y=y+D[k];X=x+D[k+1]
      if-1<Y<10 and-1<X<15 and g[Y][X]>4:g[Y][X]=0;t+=[(Y,X)]
    a,b=map(min,zip(*t));s+=[[(y-a,x-b)for y,x in t]]
 while s:
  b=T=U=V=0
  for t in s:
   for Y in 1,2:
    for X in R(15):
     f=1
     for y,x in t:
      u=y+Y;v=x+X;f+=u<3
      if u>9 or v>14 or g[u][v]:f=0;break
     if f>b:b,T,U,V=f,t,Y,X
  for y,x in T:g[U+y][V+x]=1
  s.remove(T)
 return g
