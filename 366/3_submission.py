def p(g):
 c=[0]*10;b=[[9e9,9e9,0,0]for _ in range(10)]
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   c[v]+=1;m=b[v];m[0]=min(m[0],i);m[1]=min(m[1],j);m[2]=max(m[2],i);m[3]=max(m[3],j)
  t,s,d=sorted(range(10),key=c.__getitem__)[7:];sx,sy,ex,ey=b[s];dx,dy,fx,fy=b[d]
 V=set();L=[];P=1,-1,0,0,0,0,1,-1
 for i in range(sx,ex+1):
  for j in range(sy,ey+1):
   if (i,j)in V or g[i][j]in(s,t):continue
   q=[(i,j)];V.add((i,j));C=[]
   while q:
    x,y=q.pop();C+=(x,y),
    for k in range(4):
     X=x+P[k];Y=y+P[k+4]
     if sx<=X<=ex and sy<=Y<=ey and g[X][Y]-s and(X,Y)not in V:V.add((X,Y));q+=(X,Y),
   L+=C,
 L.sort(key=lambda C:-sum(g[x][y]!=t for x,y in C))
 R=lambda a:[*zip(*a[::-1])]
 for C in L:
  xs,ys=zip(*C);m=min(xs);a=[[t]*(max(ys)-(n:=min(ys))+1)for _ in range(max(xs)-m+1)];
  for x,y in C:a[x-m][y-n]=g[x][y]
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
