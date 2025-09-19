def p(g):
 for i in range(11):
  for j in range(11):
   for k in range(11):
    if not(sum(sum(r[j:j+k+2])for r in g[i:i+k+2])+~k*20|sum(sum(r[j+1:j+k+1])for r in g[i+1:i+k+1])):
     for r in g[i+1:i+k+1]:r[j+1:j+k+1]=[2]*k
 return g