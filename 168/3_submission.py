def p(g):
 n=len(g)-1
 for r in range(n*n):
  c=r%n;r//=n
  v=g[r][c:c+2]+g[r+1][c:c+2]
  if v.count(0)==1:
   p=v.index(0);i=p>1;j=p&1;a=i*2-1;b=j*2-1;x=r+i+a;y=c+j+b
   while 0<=x<=n>=y>=0:g[x][y]=v[p-1];x+=a;y+=b
 return g
