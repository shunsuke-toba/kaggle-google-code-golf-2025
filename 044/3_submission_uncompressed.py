def p(g):
 r=sum(g,[]);g=r[:];d={};e={}
 for i,v in enumerate(g):
  if v-5:
   q=[i];g[i]=5;f=v<1;t=0,
   for j in q:
    for k in j-1,j+1,j-10,j+10:
     if g[k:k+1]==[v]:g[k]=5;q+=k,;t+=k-i,
     f*=g[k:k+1]==[5]
   if f:d[t]=i
   if r.count(v)==len(t)>1:e[t]=i,v
 for t in e:
  if t in d:
   i,v=e[t]
   for o in t:r[i+o],r[d[t]+o]=0,v
 return*zip(*[iter(r)]*10),
