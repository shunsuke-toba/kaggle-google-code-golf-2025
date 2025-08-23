def p(g):
 R=range;a=c=99;b=d=e=f=0
 for i,r in enumerate(g):
  for j,k in enumerate(r):
   if k:a=min(a,i);b=max(b,i);c=min(c,j);d=max(d,j);k-8and(e or(e:=k))and k-e and(f:=k)
 for i in R(a,b+1):
  for j in R(c,d+1):g[i][j]=[e,f][a<i<b and c<j<d]
 return g
