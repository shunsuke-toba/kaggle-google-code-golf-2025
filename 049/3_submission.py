def p(g):
 m,e=999,0
 for c in range(10):
  f=lambda r:r.count(c)
  h=[*map(list,zip(*filter(f,zip(*list(filter(f,g))))))]
  if h and(c:=len(h)*len(h[0]))<m:m,e=c,h
 return e