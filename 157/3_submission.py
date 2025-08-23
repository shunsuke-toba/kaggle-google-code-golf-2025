def p(g):
 h=10;w=15;r=range;d=1,0,-1,0,1;c=[]
 for z in r(h*w):
  y=z//w;x=z%w
  if g[y][x]>4:
   q=[(y,x)];g[y][x]=0;t=[]
   while q:
    y,x=q.pop();t+=[(y,x)]
    for i in r(4):
     Y=y+d[i];X=x+d[i+1]
     if h>Y>=0<=X<w and g[Y][X]>4:q+=[(Y,X)];g[Y][X]=0
   m=min(t)[0];n=min(t,key=lambda p:p[1])[1]
   c+=[[(y-m,x-n)for y,x in t]]
 while c:
  b=i=0;P=0,0
  for I,T in enumerate(c):
   for Y in r(3):
    for X in r(w):
     s=0
     for y,x in T:
      u=Y+y;v=X+x
      if u>=h or v>=w or g[u][v]:break
      for j in r(4):
       a=u+d[j];z=v+d[j+1];s+=h>a>=0<=z<w and g[a][z]==2
     else:
      if s>b:b=s;i=I;P=Y,X
  for y,x in c.pop(i):g[P[0]+y][P[1]+x]=1
 return g
