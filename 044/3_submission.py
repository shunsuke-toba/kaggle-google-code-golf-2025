def p(g):
 g=sum(g,[]);r=g[:];a={};b={}
 for i,c in enumerate(g):
  if c^5:
   q=[i];g[i]=5;f=c<1
   for n in q:
    for o in 1,-1,10,-10:
     m=n+o
     if 100>m>-1 and 2>m%10-n%10>-2:
      d=g[m]
      if d==c:g[m]=5;q+=m,
      elif f and d^5:f=0
     elif f:f=0
   s=tuple(j-i for j in q)
   if f and q[1:]:a[s]=i
   elif c:b[c]=(c in b or q[1:]<=[])and[0]or(s,q,i)
 for c,v in b.items():
  if v and v[0] in a:
   s,q,i=v
   for n in q:r[n]=0;r[n-i+a[s]]=c
 return[r[i*10:][:10]for i in range(10)]
