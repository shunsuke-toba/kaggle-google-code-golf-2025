def p(g):
 k=sum({*sum(g,[])})-2;r=c=0
 while g[r][c]<1:c=-~c%9;r+=c<1
 for t in 0,1,3,2:
  a=r+t//2;b=c+t%2;d=(t&2)-1;e=t%2*2-1
  while-2<a<9>b>-2 and g[a][b]-k:
   for x,y in(a,b),(a+d,b),(a,b+e):
    if-1<x<9>y>-1:g[x][y]=k
   a+=d;b+=e
 return g
