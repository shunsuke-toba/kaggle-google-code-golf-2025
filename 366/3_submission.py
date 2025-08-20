def p(g):
 c=[0]*10;b=[[99]*2+[0]*2 for _ in[0]*10]
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   c[v]+=1;m=b[v];m[0]=min(m[0],i);m[1]=min(m[1],j);m[2]=max(m[2],i);m[3]=max(m[3],j)
 *_,t,s,d=sorted(range(10),key=c.__getitem__);sx,sy,ex,ey=b[s];dx,dy,fx,fy=b[d]
 L=[];P=1,-1,0,0,0,0,1,-1
 for i in range(sx,ex+1):
  for j in range(sy,ey+1):
   if g[i][j]in(s,t):continue
   q=[(i,j)];C=[];v=g[i][j];g[i][j]=s;C+=(i,j,v),
   while q:
    x,y=q.pop()
    for k in range(4):
     X=x+P[k];Y=y+P[k+4]
     if sx<=X<=ex and sy<=Y<=ey and g[X][Y]-s:v=g[X][Y];g[X][Y]=s;q+=(X,Y),;C+=(X,Y,v),
   L+=C,
 L.sort(key=lambda C:-sum(v!=t for _,_,v in C))
 R=lambda a:[*zip(*a[::-1])]
 for C in L:
  xs,ys,_=zip(*C);m=min(xs);a=[[t]*(max(ys)-(n:=min(ys))+1)for _ in range(max(xs)-m+1)];
  for x,y,v in C:a[x-m][y-n]=v
  ok=0
  for _ in 0,1:
   for _ in'1234':
    for x in range(dx,fx-len(a)+2):
     for y in range(dy,fy-len(a[0])+2):
      if all(g[x+i][y+j]==(d,v)[v!=t]for i,r in enumerate(a)for j,v in enumerate(r)):
       for i,r in enumerate(a):
        for j,v in enumerate(r):g[x+i][y+j]=v
       ok=1;break
     if ok:break
    if ok:break
    a=R(a)
   if ok:break
   a=[r[::-1]for r in a]
 return[r[dy:fy+1]for r in g[dx:fx+1]]
