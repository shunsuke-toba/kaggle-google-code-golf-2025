def p(n):
 o=sum(n,[]);n=o[:];f={};k={}
 for i,p in enumerate(n):
  if p-5:
   q=[i];n[i]=5;u=1>p;t=0,
   for m in q:
    for m in m-1,m+1,m-10,m+10:
     if n[m:m+1]==[p]:n[m]=5;q+=m,;t+=m-i,
     u*=n[m:m+1]==[5]
   if u:f[t]=i
   if o.count(p)==len(t)>1:k[t]=i,p
 for t in k:
  if t in f:
   i,p=k[t]
   for m in t:o[i+m],o[f[t]+m]=0,p
 return*zip(*[iter(o)]*10),