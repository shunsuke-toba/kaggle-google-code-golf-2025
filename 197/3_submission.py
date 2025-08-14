def p(g):
 t=min(g,key={0}.issubset)
 for r in g:
  if{*r}>{0}:r[:]=[(*dict.fromkeys(r),)[v!=t[0]]for v in t]
 return g
