def p(g):
 for t in zip(g,g[1:],g[2:]):
  for l in range(18):
   if sum(sum(r[l:l+3])for r in t)<1:
    for r in t:r[l:l+3]=1,1,1
 return g
