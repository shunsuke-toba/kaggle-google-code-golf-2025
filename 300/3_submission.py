def p(g,e=enumerate):
 f=sum(g,[]);k=max({*f}-{0},key=f.count)
 a=b=99;c=d=0
 for i,r in e(g):
  for j,v in e(r):
   if v==k:a=min(a,i);c=max(c,i);b=min(b,j);d=max(d,j)
 return[r[b:d+1]for r in g[a:c+1]]
