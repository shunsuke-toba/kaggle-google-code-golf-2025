def p(g):
 j=g[9].index(c:=max(g[9]));k=0
 while j<10:
  g[k][j+(j<9)]=5;k=~k
  for r in g:r[j]=c
  j+=2
 return g