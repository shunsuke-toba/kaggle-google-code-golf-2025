def p(g):
 R=range;h=len(g);w=len(g[0]);d=1,0,-1,0,1;s=[]
 for y in R(h):
  for x in R(w):
   if g[y][x]>4:
    t=[(y,x)];g[y][x]=0
    for y,x in t:
     for k in R(4):
      Y=y+d[k];X=x+d[k+1]
      if h>Y>=0<=X<w and g[Y][X]>4:g[Y][X]=0;t+=[(Y,X)]
    a=min(y for y,_ in t);b=min(x for _,x in t)
    s+=[[(y-a,x-b)for y,x in t]]
 while s:
  b=-1
  for t in s:
   for Y in 1,2:
    for X in R(w):
     F=[]
     for y,x in t:
      u=y+Y;v=x+X
      if u>=h or v>=w or g[u][v]:break
      if u<3:F+=[(u,v)]
     else:
      if F and len(F)>b:b=len(F);T=t;P=Y,X
  for y,x in T:g[P[0]+y][P[1]+x]=1
  s.remove(T)
 return g
