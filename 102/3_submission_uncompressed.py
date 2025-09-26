def p(g):
 for s in range(11):
  for y in range(11):
   for x in range(11):
    if not(sum(sum(r[x:x+s+2])for r in g[y:y+s+2])-20*s-20|sum(sum(r[x+1:x+s+1])for r in g[y+1:y+s+1])):
     for r in g[y+1:y+s+1]:r[x+1:x+s+1]=[2]*s
 return g