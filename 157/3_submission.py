def p(g):
 R=range;D=1,0,-1,0,1;s=[]
 for Y in R(10):
  for X in R(15):
   if g[Y][X]>4:
    t=[(0,0)];g[Y][X]=0
    for y,x in t:
     for k in R(4):
      u=Y+y+D[k];v=X+x+D[k+1]
      if u<10 and-1<v<15 and g[u][v]>4:g[u][v]=0;t+=(u-Y,v-X),
    s+=t,
 while s:
  T,U,V=max(((t,Y,X,sum(Y+y<3 for y,x in t))for t in s for Y in(1,2)for X in R(15)if all(15>X+x and g[Y+y][X+x]<1 for y,x in t)),key=lambda q:q[3])[:3]
  for y,x in T:g[U+y][V+x]=1
  s.remove(T)
 return g
