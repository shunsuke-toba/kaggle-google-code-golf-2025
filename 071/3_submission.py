def p(g,a=0):
 for r in g:
  for i,v in enumerate(r):
   if a and 0<v!=a:r[i]=r[~i+t]
   elif v>a:a=v;t=i-r[::-1].index(v)
 return g