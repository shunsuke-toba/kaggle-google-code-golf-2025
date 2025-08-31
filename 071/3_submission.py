def p(g,a=0):
 for r in g:
  if a<1:s=r.index(a:=max(r))+15-r[::-1].index(a)
  for i in range(16):
   if 0<r[i]!=a:r[i]=r[s-i]
 return g