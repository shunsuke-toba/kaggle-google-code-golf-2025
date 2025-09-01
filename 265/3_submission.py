def p(g):
 for a,b in zip(g,g[1:]):
  t=5,*map(sum,zip(a,b))
  for j in range(17):
   if t[j]|t[6]>4>t[j+1]|t[j+2]:a[j:j+2]=b[j:j+2]=2,2
 return g