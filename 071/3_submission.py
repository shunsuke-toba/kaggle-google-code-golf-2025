def p(g,E=enumerate):
 for r in g:
  if(t:=[i for i,x in E(r)if x]):s=t[0]+t[-1];a=r[t[0]];break
 for r in g:
  for i,x in E(r):
   if 0<x!=a:r[i]=r[s-i]
 return g
