def p(g,a=0):
 for r in g:
  if 1>a<(a:=max(r)):s=r.index(a)+15-r[::-1].index(a)
  for i in range(16):
   if 0<r[i]!=a:r[i]=r[s-i]
 return g