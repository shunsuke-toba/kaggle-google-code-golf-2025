def p(g,a=0):
 for r in g:
  for i,v in enumerate(r):
   if a<1:a=v;t=i-r[::-1].index(v)
   elif 0<v!=a:r[i]=r[~i+t]
 return g