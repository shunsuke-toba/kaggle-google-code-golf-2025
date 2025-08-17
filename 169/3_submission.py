def p(g):
 d=1,0,-1,0,1;k=100
 while k:
  k-=1;i=k//10;j=k%10
  if g[i][j]==5:
   q=[(i,j)];g[i][j]=0
   for i,j in q:
    for n in 0,1,2,3:
     x,y=i+d[n],j+d[n+1]
     if 0<=x<10>y>=0<g[x][y]==5:g[x][y]=0;q+=[(x,y)]
   for i,j in q:g[i][j]=5-len(q)
 return g
