def p(g):
 for n in range(324):
  i=n//18;j=n%18;t=g[i:i+3]
  if sum(sum(r[j:j+3])for r in t)<1:
   for r in t:r[j:j+3]=1,1,1
 return g
