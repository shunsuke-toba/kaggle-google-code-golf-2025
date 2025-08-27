def p(g):
 for r,b in zip(g,g[1:]):
  j=len(r)
  while j:
   if 0<(v:=r[j:=j-1])in b[j+1:]:r[j:j+2]=0,v
 return g