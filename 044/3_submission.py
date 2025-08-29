def p(g):
 r=sum(g,[]);g=r*1;d,e={},{}
 for i,v in enumerate(g):
  if v^5:
   q=[i];g[i]=5;f=v<1
   for j in q:
    for k in j+1,j-1,j+10,j-10:
     try:
      if g[k]==v:g[k]=5;q+=k,
      f*=g[k]==5
     except:f=0
   t=tuple(x-i for x in q)
   if f:d[t]=i
   if r.count(v)==len(t)>1:e[t]=i,v
 for t in {*e}&{*d}:
  i,v=e[t]
  for o in t:r[i+o]=0;r[d[t]+o]=v
 return[*zip(*[iter(r)]*10)]