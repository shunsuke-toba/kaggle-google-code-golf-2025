def p(g):
 o=[[0]*len(g[0])for _ in g]
 for _ in 0,1:
  for x,k in enumerate(zip(*g)):
   if{*k}=={c:=k[0]}!={0}:
    for r,q in zip(g,o):q[x-(c in r[:x])]=q[x+(c in r[x+1:])]=c
  g,o=[*zip(*g)],[*map(list,zip(*o))]
 return o
