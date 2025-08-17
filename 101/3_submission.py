def p(g):
 h=len(g);w=len(g[0]);R=range;E=enumerate;v=set();b=0
 for i in R(h):
  for j in R(w):
   if g[i][j]>0and(i,j)not in v:
    q=[(i,j)];v.add((i,j));c=[];a=d=0
    while q:
     x,y=q.pop(0);c+=x,y;u=g[x][y];a|=u<2;d|=u>1
     for X,Y in((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
      if 0<=X<h and 0<=Y<w and g[X][Y]and(X,Y)not in v:v.add((X,Y));q+=[(X,Y)]
    if a&d and not b:b=c
 if not b:return g
 x0,x1=min(X:=b[::2]),max(X);y0,y1=min(Y:=b[1::2]),max(Y)
 P=[r[y0:y1+1]for r in g[x0:x1+1]]
 B1=[(i,j)for i,r in E(P)for j,u in E(r)if u&1];B2=[(i,j)for i,r in E(P)for j,u in E(r)if u>1]
 S={(i,j)for i in R(h)for j in R(w)if g[i][j]==2}-set(zip(b[::2],b[1::2]))
 X,Y=zip(*B2);a,b=min(X),max(X);c,d=min(Y),max(Y)
 for k in R(max(h,w),0,-1):
  for r0 in R(-a*k,h-b*k-k+1):
   for c0 in R(-c*k,w-d*k-k+1):
    U={(i,j)for r,c in B2 for i in R(r0+r*k,r0+(r+1)*k) for j in R(c0+c*k,c0+(c+1)*k)}
    if U-S:continue
    if any(0<=i<h and 0<=j<w and g[i][j] for r,c in B1 for i in R(r0+r*k,r0+(r+1)*k) for j in R(c0+c*k,c0+(c+1)*k)):continue
    for r,m in E(P):
     for c,n in E(m):
      for i in R(r0+r*k,r0+(r+1)*k):
       for j in R(c0+c*k,c0+(c+1)*k):
        if 0<=i<h and 0<=j<w:g[i][j]=n
    S-=U
 return g
