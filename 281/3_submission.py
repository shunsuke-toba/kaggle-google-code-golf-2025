def p(g):
 a=c=9;d=0;p=[];E=enumerate
 for y,m in E(g):
  for x,k in E(m):
   if k:a=min(a,y);b=y;c=min(c,x);d=max(d,x);p+=[k]*(k not in p+[8])
 for y in range(a,b+1):
  for x in range(c,d+1):g[y][x]=p[a<y<b>-1<c<x<d]
 return g