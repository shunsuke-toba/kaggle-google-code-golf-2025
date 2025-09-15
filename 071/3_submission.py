def p(g,a=0):
 for r in g:
  for i,v in enumerate(r):
   if a<1:t=i-r[::-1].index(a:=v)
   if 0<v!=a:r[i]=r[~i+t]
 return g