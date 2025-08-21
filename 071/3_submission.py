def p(g,E=enumerate):
 a=sum(g,[])
 for b in{*a}-{0}:
  if a.count(b)==sum(b in r for r in g)*sum(b in c for c in zip(*g)):break
 r=next(r for r in g if sum(r)and b not in r)
 t=[i for i,x in E(r)if x];s=t[0]+t[-1]
 for r in g:
  for c,x in E(r):
   if x==b:r[c]=r[s-c]
 return g
