def p(g):
 for y in range(11):
  for x in range(11):
   for s in range(11):
    if not(sum(sum(row[x:x+s+2])for row in g[y:y+s+2])+~s*20|sum(sum(row[x+1:x+s+1])for row in g[y+1:y+s+1])):
     for row in g[y+1:y+s+1]:row[x+1:x+s+1]=[2]*s
 return g