def p(g):
 f=sum(g,[]);k=sum({*f})-2
 for i,v in enumerate(f):
  if v-2:continue
  a,b=divmod(i,9);d=1-2*(g[a-1][b]<1);e=1-2*(g[a][b-1]<1)
  while-1<a<9>-1<b<9:
   for x,y in(a,b),(a+d,b),(a,b+e):
    if-1<x<9>y>-1:g[x][y]=k
   a+=d;b+=e
 return g
