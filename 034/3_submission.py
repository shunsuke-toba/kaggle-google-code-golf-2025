def p(g):
 while 2in(f:=sum(g,[])):
  k,a=sum({*f})-2,f.index(2);d,e=f[a+9]<1or-1,f[a+1]<1or-1;b=a%9;a//=9
  for x,y in(a,b),(a+d,b),(a,b+e):
   while 9>x>-1<y<9:g[x][y]=k;x+=d;y+=e
 return g