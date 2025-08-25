def p(g):
 R=range;D=1,0,-1,0,1;s=[]
 for y in R(10):
  for x in R(15):
   if g[y][x]>4:
    t=[(0,0)];g[y][x]=0
    for Y,X in t:
     for k in R(4):
      u=y+Y+D[k];v=x+X+D[k+1]
      if 10>u>-1<v<15 and g[u][v]>4:g[u][v]=0;t+=[(u-y,v-x)]
    s+=t,
 while s:
  b=-1
  for t in s:
   for Y in 1,2:
    for X in R(15):
     if all(10>(u:=Y+y)>-1<(v:=X+x)<15 and g[u][v]<1 for y,x in t) and (f:=sum(Y+y<3 for y,x in t))>b:
      b=f;T,U,V=t,Y,X
  for y,x in T:g[U+y][V+x]=1
  s.remove(T)
 return g
