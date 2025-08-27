def p(g):
 g=sum(g,[]);r=g[:];a={};s=[]
 for i,c in enumerate(g):
  if c^5:
   q=[i];g[i]=5;b=c<1
   for n in q:
    for m in n+1,n-1,n+10,n-10:
     if-1<m<100 and 2>m%10-n%10>-2:
      if(x:=g[m])==c:g[m]=5;q+=m,
      elif b*(x-5):b=0
     else:b=0
   t=tuple(x-i for x in q)
   if b:a[t]=i
   elif r.count(c)==len(t)>1:s+=[(t,i,c)]
 for t,i,c in s:
  if t in a:
   for o in t:r[i+o]=0;r[a[t]+o]=c
 return[*zip(*[iter(r)]*10)]
