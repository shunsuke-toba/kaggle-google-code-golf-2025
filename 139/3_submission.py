def p(g):
 a=any(g[8])
 for r,c in (1,2*a),(4+2*a,5):
  for R in g[r:r+3]:R[c:c+3]=[x or 7 for x in R[c:c+3]]
 return g

