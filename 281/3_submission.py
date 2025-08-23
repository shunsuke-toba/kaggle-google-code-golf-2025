def p(g):
 a=c=9;b=d=o=i=0;E=enumerate
 for y,r in E(g):
  for x,k in E(r):
   if k:a=min(a,y);b=y;c=min(c,x);d=max(d,x);k-8 and(o or(o:=k))and k-o and(i:=k)
 for y in range(a,b+1):
  for x in range(c,d+1):g[y][x]=[o,i][a<y<b and c<x<d]
 return g
