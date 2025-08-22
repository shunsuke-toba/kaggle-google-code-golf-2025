def p(g):
 d=1,0,-1,0;k=99
 while~k:
  i=k//10;j=k%10;k-=1
  if g[i][j]>4:
   q=[(i,j)];g[i][j]=0
   for i,j in q:
    for n in 0,1,2,3:
     x,y=i+d[n],j+d[n-1]
     if-1<x<10>y>-1<g[x][y]>4:g[x][y]=0;q+=[(x,y)]
   for i,j in q:g[i][j]=5-len(q)
 return g