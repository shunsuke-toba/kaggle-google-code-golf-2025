def p(g,r=range):
 for a,b,c in zip(g,g[1:],g[2:]):
  for i in r(len(b)-1):
   if a[i]==b[i]==c[i]==b[i+1]:b[i+1]=0
 return g
