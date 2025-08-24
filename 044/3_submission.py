def p(g):
 g=sum(g,[]);r=g[:];a={};b=()
 for i,c in enumerate(g):
  if c^5:
   q=[i];g[i]=5;f=c<1
   for n in q:
    for m in n+1,n-1,n+10,n-10:
     if-1<m<100 and 2>m%10-n%10>-2:
      d=g[m]
      if d==c:g[m]=5;q+=m,
      elif f*d^5:f=0
     else:f=0
   t=tuple(x-i for x in q)
   if f:a[t]=i
   elif c and r.count(c)==len(q)>1:b+=((t,q,c),)
 for s,q,c in b:
  if s in a:
   for n in q:r[n]=0;r[n+a[s]-q[0]]=c
 return[*map(list,zip(*[iter(r)]*10))]
