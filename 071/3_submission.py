def p(g,E=enumerate):
 a=0
 for r in g:
  if a<1 and (a:=max(r)):s=r.index(a)+len(r)+~r[::-1].index(a)
  for i,x in E(r):
   if 0<x!=a:r[i]=r[s-i]
 return g
