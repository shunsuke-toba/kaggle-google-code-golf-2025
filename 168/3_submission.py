def p(g):
 n=len(g)
 for r in range(n-1):
  for c in range(n-1):
   v=g[r][c:c+2]+g[r+1][c:c+2]
   if v.count(0)==1:
    i,j=divmod(v.index(0),2);k=v[i*2+j-1];a=i*2-1;b=j*2-1;x=r+i+a;y=c+j+b
    while 0<=x<n>y>=0:g[x][y]=k;x+=a;y+=b
 return g