def p(g,*b):
 for a in g:
  if a==b:a[a[::2]>a[1::2]::2]=g[0][::2]
  b=a
 return g