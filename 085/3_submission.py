def p(g):
 for a,b in zip(g,g[1:]):
  for i in range(len(b)):b[i]*=(a[i-1]==a[i]==b[i-1]>0)^1
 return g
