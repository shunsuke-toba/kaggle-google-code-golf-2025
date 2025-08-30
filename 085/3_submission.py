def p(g):
 for a,b in zip(g,g[1:]):
  if a==b:b[a[::2]>a[1::2]::2]=g[0][::2]
 return g