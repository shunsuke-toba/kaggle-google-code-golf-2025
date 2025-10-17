def p(n):
 o=sum(n,[]);n=o[:];f={};e={}
 for i,v in enumerate(n):
  if v-5:
   q=[i];n[i]=5;u=1>v;t=0,
   for j in q:
    for k in j-1,j+1,j-10,j+10:
     if n[k:k+1]==[v]:n[k]=5;q+=k,;t+=k-i,
     u*=n[k:k+1]==[5]
   if u:f[t]=i
   if o.count(v)==len(t)>1:e[t]=i,v
 for t in e:
  if t in f:
   i,v=e[t]
   for k in t:o[i+k],o[f[t]+k]=0,v
 return*zip(*[iter(o)]*10),