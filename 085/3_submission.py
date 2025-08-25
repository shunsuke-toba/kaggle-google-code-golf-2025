def p(g):
 for a,b in zip(g,g[1:]):
  j=0
  for c in b:b[j]*=(a[j-1]==a[j]==b[j-1]>0)^1;j+=1
 return g