def p(g,a=0):
 for r in g:
  if 1>a<(a:=max(r)):s=r.index(a)+len(r)+~r[::-1].index(a)
  for i,x in enumerate(r):
   if 0<x!=a:r[i]=r[s-i]
 return g