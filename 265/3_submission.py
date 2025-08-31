def p(g):
 for a,b in zip(g,g[1:]):
  t=[10,*((x&-3)+(y&-3)for x,y in zip(a,b)),10]
  for j in range(17):
   if t[j+1]==t[j+2]==0 and t[j]|t[j+3]^10:a[j:j+2]=b[j:j+2]=2,2
 return g