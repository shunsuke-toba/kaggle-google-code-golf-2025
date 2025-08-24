def p(g):
 a=c=9;b=d=o=0;e=enumerate;r=range
 for y,m in e(g):
  for x,k in e(m):
   if k:a=min(a,y);b=y;c=min(c,x);d=max(d,x);k-8 and(o:=o or k)-k and(i:=k)
 for y in r(a,b+1):
  for x in r(c,d+1):g[y][x]=[o,i][a<y<b and c<x<d]
 return g
