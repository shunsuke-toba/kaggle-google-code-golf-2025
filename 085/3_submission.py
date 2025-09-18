def p(g):
 a=0
 for b in g:
  if a==b:b[a[::2]>a[1::2]::2]=g[0][::2]
  a=b
 return g