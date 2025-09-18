def p(g):
 x=o=0;t=*zip(*g),
 for k in t:
  if c:=min(k):
   for r,q in zip(g,o:=o or[[0]*len(r)for r in g]):q[x]=q[x+(c in r[x+1:])-(c in r[:x])]=c
  x+=1
 return o or[*zip(*p(t))]