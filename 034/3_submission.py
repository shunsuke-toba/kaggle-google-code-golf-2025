def p(g):
 f=sum(g,[])
 while 2in f:
  f[i:=f.index(2)]=k=sum({*f})-2;a,b=i//9,i%9;d=f[i+9]<1or-1;e=f[i+1]<1or-1
  for _ in g:
   for x,y in(a,b),(a+d,b),(a,b+e):
    if 9>x>-1<y<9:g[x][y]=k
   a+=d;b+=e
 return g