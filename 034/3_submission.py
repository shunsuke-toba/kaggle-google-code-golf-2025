def p(g):
 k=sum({*sum(g,[])})-2;r=c=0
 while g[r][c]<1:c=(c+1)%9;r+=c<1
 for i,j in[(i,j)for i in(0,1)for j in(0,1)if g[r+i][c+j]-k]:
  a,b=r,c
  while-2<a<9>b>-2:
   for u in a,a+1:
    for v in b,b+1:
     if-1<u<9>v>-1:g[u][v]=k
   a+=i*2-1;b+=j*2-1
 return g
