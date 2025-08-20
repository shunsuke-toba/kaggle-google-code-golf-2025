def p(g):
 b=g[0][0];h=len(g);w=len(g[0]);d=(1,0,-1,0,0,1,0,-1)
 v=[[0]*w for _ in g];c=[]
 for y in range(h):
  for x in range(w):
   if g[y][x]-b and not v[y][x]:
    q=[(y,x)];v[y][x]=1;s=[]
    while q:
     y0,x0=q.pop();s+=[(y0,x0)]
     for i in range(4):
      ny=y0+d[i];nx=x0+d[i+4]
      if 0<=ny<h and 0<=nx<w and g[ny][nx]-b and not v[ny][nx]:v[ny][nx]=1;q.append((ny,nx))
    c+=s,
 P=[a for a in c if (max(y for y,_ in a)-min(y for y,_ in a)+1)*(max(x for _,x in a)-min(x for _,x in a)+1)-len(a)][0]
 R=[a for a in c if a is not P];S=set(P)
 pc={g[y][x] for y,x in P};rc={g[y][x] for a in R for y,x in a};B=[x for x in pc if x in rc][0]
 for y,x in P:
  if g[y][x]==B and all((y+d[i],x+d[i+4]) in S for i in range(4)):
   by,bx=y,x;break
 t={(y-by,x-bx):g[y][x] for y,x in P}
 for y,x in P:g[y][x]=b
 for a in R:
  ys,xs=zip(*a);T,Bm=min(ys),max(ys);L,Rm=min(xs),max(xs)
  bs=[(y,x) for y,x in a if g[y][x]==B]
  for y,x in bs:
   for (dy,dx),c0 in t.items():
    Y,X=y+dy,x+dx
    if T<=Y<=Bm and L<=X<=Rm:g[Y][X]=c0
   for i in range(4):
    dy,dx=d[i],d[i+4];c1=t.get((dy,dx));c2=t.get((2*dy,2*dx))
    if c1==c2!=None:
     Y,X=y+dy,x+dx
     while T<=Y<=Bm and L<=X<=Rm:g[Y][X]=c1;Y+=dy;X+=dx
 return g
