def p(g):
 for a in g*2+[9*[8]]:
  for b in g:
   for i in range(21):b[i]=b[i]or(a[i-3]==b[i-3]>0)*a[i]
 return g