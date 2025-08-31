def p(g):
 for a,b in zip(g,g[1:]):
  t=1,*map(lambda x,y:x+y>4,a,b),1
  for j in range(17):
   if t[j+1]|t[j+2]<t[j]|t[6]:a[j:j+2]=b[j:j+2]=2,2
 return g