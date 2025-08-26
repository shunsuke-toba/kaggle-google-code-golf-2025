def p(g):
 f=sum(g,[]);k=sum({*f})-2
 while 2 in f:
  f[i:=f.index(2)]=k
  a=i//9;b=i%9
  d=g[a-1][b]>0 or-1;e=g[a][b-1]>0 or-1
  for _ in[0]*9:
   for x,y in(a,b),(a+d,b),(a,b+e):
    if 9>x>-1<y<9:g[x][y]=k
   a+=d;b+=e
 return g