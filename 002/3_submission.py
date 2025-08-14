def p(j):
 for r in j:r[:]=[x or 4for x in r]
 for _ in range(64):
  for i,r in enumerate(j):
   for k in range(len(r)):
    if r[k]==4and(i<1or j[i-1][k]<1):r[k]=0
  j[:]=[list(r)for r in zip(*j[::-1])]
 return j