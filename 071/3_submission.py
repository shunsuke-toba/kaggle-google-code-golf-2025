def p(g,E=enumerate):
 a=sum(g,[])
 b=next(c for c in{*a}-{0}if a.count(c)==sum(c in r for r in g)*sum(c in r for r in zip(*g)))
 s=min(t[0]+t[-1]for r in g if b not in r if(t:=[i for i,x in E(r)if x]))
 for r in g:
  for i,x in E(r):
   if x==b:r[i]=r[s-i]
 return g
