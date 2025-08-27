def p(g):
 for r,b in zip(g,g[1:]):
  j=len(r)
  while j:
   if (v:=r[j:=j-1]) and v in b[j+1:]:r[j],r[j+1]=0,v
 return g
