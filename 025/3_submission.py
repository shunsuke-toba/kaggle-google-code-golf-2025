def p(g):
 o=0;x=0
 for k in(t:=[*zip(*g)]):
  if{*k}<{0,c:=k[0]}:
   for r,q in zip(g,o:=o or[[0]*len(r)for r in g]):q[x]=q[x+(c in r[x+1:])-(c in r[:x])]=c
  x+=1
 return o or[*zip(*p(t))]