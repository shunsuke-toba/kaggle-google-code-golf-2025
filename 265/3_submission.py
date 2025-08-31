def p(g):
 for a,b in zip(g,g[1:]):
  t=8,*map(lambda x,y:(x+y)&-3,a,b),8
  for j in range(17):
   if t[j+1]<1>t[j+2] and t[j]|t[j+3]^8:a[j:j+2]=b[j:j+2]=2,2
 return g