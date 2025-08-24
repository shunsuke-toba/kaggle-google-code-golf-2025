def p(g):
 for a,b,c in zip(g,g[1:],g[2:]):
  for i in range(len(b)-1):b[i+1]*=(a[i]==b[i]==c[i]==b[i+1])^1
 return g
