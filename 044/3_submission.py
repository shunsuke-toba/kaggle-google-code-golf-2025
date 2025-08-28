def p(g):
 g=sum(g,[]);r=g[:];d,e={},{}
 for i,v in enumerate(g):
  if v^5:
   q=[i];g[i]=5;f=v<1
   for j in q:
    for k in j+1,j-1,j+10,j-10:
     try:x=g[k]
     except:x=5;f=0
     if x==v:g[k]=5;q+=k,
     else:f*=x==5
   t=tuple(x-i for x in q)
   if f:d[t]=i
   elif r.count(v)==len(t)>1:e[t]=i,v
 for t in e.keys()&d:
  i,v=e[t]
  for o in t:r[i+o]=0;r[d[t]+o]=v
 return[*zip(*[iter(r)]*10)]