def p(g):
 r=c=0;k=sum({*sum(g,[])})-2
 while g[r][c]<1:c+=1;r+=c>8;c%=9
 for i,j in[(i,j)for i in(0,1)for j in(0,1)if g[r+i][c+j]==2]:
  a,b=r,c
  while-2<a<9>-2<b<9:
   for u in a,a+1:
    for v in b,b+1:
     if 0<=u<9>v>=0:g[u][v]=k
   a+=i*2-1;b+=j*2-1
 return g
