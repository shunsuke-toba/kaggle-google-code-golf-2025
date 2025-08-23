def p(g):
 g=sum(g,[]);r=g[:];a={};b={}
 for i,c in enumerate(g):
  if c^5:
   q=[i];g[i]=5;f=c<1
   for n in q:
    for m in n+1,n-1,n+10,n-10:
     if-1<m<100 and 2>m%10-n%10>-2:
      if(d:=g[m])==c:g[m]=5;q+=m,
      elif f*d^5:f=0
     elif f:f=0
   s=tuple(x-i for x in q)
   if f*q[1:]:a[s]=i
   elif c:b[c]=(c in b or 2>len(q))and[0]or(s,q)
 for c in b:
  if(v:=b[c])and v[0]in a:
   s,q=v;t=a[s]-q[0]
   for n in q:r[n],r[n+t]=0,c
 return[r[i*10:][:10]for i in range(10)]
