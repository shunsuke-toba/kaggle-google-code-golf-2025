def p(g):
 for r in g:
  for t in g:r[:]=[map(max,r,t),r][any((a^b)*a*b for a,b in zip(r,t))]
 return g