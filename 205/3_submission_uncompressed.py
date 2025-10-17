def p(l):
 for o in range(10,5,-1):
  for n in range(10,5,-1):
   for r in range(len(l)-o):
    for f in range(len(l[0])-n):
     d=[r[f:f+n]for r in l[r:r+o]]
     if len({r[f]for r in d for f in range(n)})<3:
      for r,f in[(r,f)for r in d for f in range(n)if r[f]-r[0]]:
       for e in d:e[f]=r[f]
       for e in range(n):r[e]=r[f]
      return d