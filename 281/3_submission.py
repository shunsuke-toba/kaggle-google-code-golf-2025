def p(g):
 a=c=9;b=d=0;p=[];E=enumerate
 for y,r in E(g):
  for x,k in E(r):
   if k:a=min(a,b:=y);c=min(c,x);d=max(d,x);p+=[k]*(k not in p+[8])
 for y in range(a,b+1):
  for x in range(c,d+1):g[y][x]=p[a<y<b>=c<x<d]
 return g