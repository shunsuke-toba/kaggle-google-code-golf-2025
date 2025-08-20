def p(g,e=enumerate):
 w=len(g[0]);o=[w*[0]for _ in g]
 for _ in 0,1:
  for x,k in e(zip(*g)):
   if{*k}=={c:=k[0]}!={0}:
    for y,r in e(g):
     q=o[y];q[x-(c in r[:x])]=q[x]=q[x+(c in r[x+1:])]=c
  g,o=[*zip(*g)],[*map(list,zip(*o))]
 return o
