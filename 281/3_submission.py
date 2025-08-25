def p(g):
 a=c=9;d=o=0;e=enumerate
 for y,m in e(g):
  for x,k in e(m):
   if k:a=min(a,y);b=y;c=min(c,x);d=max(d,x);k-8 and(o:=o or k)-k and(i:=k)
 for y in range(a,b+1):
  for x in range(c,d+1):g[y][x]=[o,i][a<y<b and c<x<d]
 return g
