def p(g,e=enumerate):
 g=[r*2 for _ in(0,1)for r in g]
 for r,R in e(g):
  for c,v in e(R):
   if v%8:
    for I in-1,1:
     for J in-1,1:
      if len(g)>r+I>=0<=c+J<len(g[0])and g[r+I][c+J]<1:g[r+I][c+J]=8
 return g
