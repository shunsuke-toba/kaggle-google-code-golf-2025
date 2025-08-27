def p(g):
 g=sum(g,[]);r=g[:];d,b={},{}
 for i,c in enumerate(g):
  if c^5:
   q=[i];g[i]=5;e=c<1
   for n in q:
    for m in n+1,n-1,n+10,n-10:
     if-1<m<100 and 2>m%10-n%10>-2:
      if(x:=g[m])==c:g[m]=5;q+=m,
      elif e*(x-5):e=0
     else:e=0
   t=tuple(x-i for x in q)
   if e:d[t]=i
   elif r.count(c)==len(t)>1:b[t]=i,c
 for t in b.keys()&d:
  i,c=b[t]
  for o in t:r[i+o]=0;r[d[t]+o]=c
 return[*zip(*[iter(r)]*10)]