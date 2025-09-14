def p(g):
 for a in range(10,5,-1):
  for b in range(10,5,-1):
   for y in range(len(g)-a):
    for x in range(len(g[0])-b):
     s=[r[x:x+b]for r in g[y:y+a]]
     if len({r[x]for r in s for x in range(b)})<3:
      for r,x in[(r,x)for r in s for x in range(b)if r[x]-r[0]]:
       for t in s:t[x]=r[x]
       r[:]=[r[x]]*b
      return s