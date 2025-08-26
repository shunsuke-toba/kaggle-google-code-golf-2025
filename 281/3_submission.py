def p(g):
 a=c=9;d=0;p=[];e=enumerate
 for y,m in e(g):
  for x,k in e(m):
   if k:a=min(a,y);b=y;c=min(c,x);d=max(d,x);p+=[k]*(k^8>0)*(k not in p)
 for y in range(a,b+1):
  for x in range(c,d+1):g[y][x]=p[a<y<b and c<x<d]
 return g
