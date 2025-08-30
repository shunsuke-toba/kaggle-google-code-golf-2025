def p(g):
 for r in g:
  for t in g:
   if all((a^b)*a*b<1for a,b in zip(r,t)):r[:]=map(max,r,t)
 return g