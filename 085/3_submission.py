def p(g):
 for a,b,c in zip(g,g[1:],g[2:]):
  i=p=0
  while b[i:]:b[i]*=p^1;p=a[i]==b[i]==c[i]>0;i+=1
 return g
