def p(g):
 z=zip;o=[[0]*len(g)for g in g]
 for _ in 0,1:
  for x,k in enumerate(z(*g)):
   if{*k}=={c:=k[0]}!={0}:
    for r,q in z(g,o):q[x-(c in r[:x])]=q[x+(c in r[x+1:])]=c
  g,o=[*z(*g)],[*map(list,z(*o))]
 return o