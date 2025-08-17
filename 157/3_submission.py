def p(g):
 h=len(g);w=len(g[0]);r=range;d=(1,0,-1,0,1);c=[]
 for y in r(h):
  for x in r(w):
   if g[y][x]==5:
    q=[(y,x)];g[y][x]=0;t=[]
    while q:
     Y,X=q.pop();t+=[(Y,X)]
     for i in r(4):
      ny,nx=Y+d[i],X+d[i+1]
      if 0<=ny<h and 0<=nx<w and g[ny][nx]==5:g[ny][nx]=0;q+=[(ny,nx)]
    m=min(y for y,x in t);n=min(x for y,x in t)
    c+=[[(y-m,x-n)for y,x in t]]
 while c:
  b=-1
  for i,t in enumerate(c):
   for Y in r(3):
    for X in r(w):
     ok=1;s=0
     for y,x in t:
      u=Y+y;v=X+x
      if u>=h or v>=w or g[u][v]:ok=0;break
      for j in r(4):
       ny,nx=u+d[j],v+d[j+1]
       if 0<=ny<h and 0<=nx<w and g[ny][nx]==2:s+=1
     if ok and s>b:b=s;I=i;Y0=Y;X0=X
  for y,x in c.pop(I):g[Y0+y][X0+x]=1
 return g
