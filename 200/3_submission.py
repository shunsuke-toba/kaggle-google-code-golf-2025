def p(g):
 j=g[k:=9].index(c:=max(g[k]))
 while j<10:
  g[k:=~k][j+(j<9)]=5
  for r in g:r[j]=c
  j+=2
 return g