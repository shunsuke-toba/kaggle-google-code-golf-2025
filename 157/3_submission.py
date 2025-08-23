def p(g):
 r=range;d=1,0,-1,0,1;h=len(g);w=len(g[0]);s=[]
 for i in r(h*w):
  y,x=divmod(i,w)
  if g[y][x]>4:
   t=[(y,x)];g[y][x]=0
   for y,x in t:
    for k in r(4):
     Y=y+d[k];X=x+d[k+1]
     if h>Y>=0<=X<w and g[Y][X]>4:t+=[(Y,X)];g[Y][X]=0
   m=min(t);n=min(t,key=lambda p:p[1])
   s+=[[(y-m[0],x-n[1])for y,x in t]]
 while s:
  b=-1
  for t in s:
   for Y in(1,2):
    for X in r(w):
     s2=0
     for y,x in t:
      u=y+Y;v=x+X
      if u>=h or v>=w or g[u][v]:break
      for j in r(4):
       a=u+d[j];z=v+d[j+1];s2+=h>a>=0<=z<w and g[a][z]==2
     else:
      if s2>b:b=s2;T=t;P=Y,X
  for y,x in T:g[P[0]+y][P[1]+x]=1
  s.remove(T)
 return g
