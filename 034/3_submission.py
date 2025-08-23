def p(g):
 k=sum({*sum(g,[])})-2;r=c=0
 while g[r][c]<1:c=(c+1)%9;r+=c<1
 for t in[t for t in(0,1,3,2)if g[r+t//2][c+t%2]-k]:
  a,b=r,c
  while-2<a<9>b>-2:
   for u in a,a+1:
    for v in b,b+1:
     if-1<u<9>v>-1:g[u][v]=k
   a+=t-t%2-1;b+=t%2*2-1
 return g