def p(g,R=range):
 for i in R(10):
  for j in R(10):
   if g[i][j]<1:
    q=[(i,j)];g[i][j]=1;a=b=i;c=d=j;k=0
    while q:
     x,y=q.pop();k+=1;a=min(a,x);b=max(b,x);c=min(c,y);d=max(d,y)
     for u,v in((1,0),(0,1),(-1,0),(0,-1)):
      X=x+u;Y=y+v
      if 0<=X<10 and 0<=Y<10 and g[X][Y]<1:g[X][Y]=1;q.append((X,Y))
    h=b-a+1;w=d-c+1
    if h*w==k and max(h,w)<9:r=a;C=c;H=b;W=d;break
  else:continue
  break
 n=max(H-r+1,W-C+1)
 for x,y in((r-1,C),(H+1,C),(r,C-1),(r,W+1)):
  if 0<=x<10 and 0<=y<10 and g[x][y]:f=g[x][y];break
 for i in R(10):
  for j in R(10):
   dr=max(r-i,0,i-H);dc=max(C-j,0,j-W);d=max(dr,dc)
   g[i][j]=f if d%(n+1)==1 else 5
 return g
