def p(g):
 h=len(g);w=len(g[0]);r=range;d=1,0,-1,0,1;c=[]
 for z in r(h*w):
  y=z//w;x=z%w
  if g[y][x]>4:
   q=[y,x];g[y][x]=0;t=[]
   while q:
    x=q.pop();y=q.pop();t+=y,x
    for i in r(4):
     Y=y+d[i];X=x+d[i+1]
     if 0<=Y<h and 0<=X<w and g[Y][X]>4:g[Y][X]=0;q+=Y,X
   m=min(t[::2]);n=min(t[1::2])
   c+=[[[t[i]-m,t[i+1]-n]for i in r(0,len(t),2)]]
 while c:
  b=0
  for I,T in enumerate(c):
   for Y in r(3):
    for X in r(w):
     s=0
     for y,x in T:
      u=Y+y;v=X+x
      if u>=h or v>=w or g[u][v]:break
      for j in r(4):
       a=u+d[j];z=v+d[j+1];s+=0<=a<h and 0<=z<w and g[a][z]==2
     else:
      if s>b:b=s;i=I;Y0=Y;X0=X
  for y,x in c.pop(i):g[Y0+y][X0+x]=1
 return g
