def p(g):
 r=sum(g,[]);g=r[:];d={};e={};c=r.count
 for i,v in enumerate(g):
  if v-5:
   q=[i];g[i]=5;f=v<1;t=0,
   for j in q:
    for k in j-1,j+1,j-10,j+10:
     if g[k:k+1]==[v]:g[k]=5;q+=k,;t+=k-i,
     f*=5in g[k:k+1]
   if f:d[t]=i
   if len(t)==c(v)>1:e[t]=i,v
 for t in d:
  if t in e:
   i,v=e[t];a=d[t]
   for o in t:r[i+o],r[a+o]=0,v
 return*zip(*[iter(r)]*10),