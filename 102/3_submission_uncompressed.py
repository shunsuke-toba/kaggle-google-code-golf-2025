def p(g):
 for a in range(11):
  for b in range(11):
   for c in range(11):
    if not(sum(sum(r[c:c+a+2])for r in g[b:b+a+2])-20*a-20|sum(sum(r[c+1:c+a+1])for r in g[b+1:b+a+1])):
     for r in g[b+1:b+a+1]:r[c+1:c+a+1]=[2]*a
 return g