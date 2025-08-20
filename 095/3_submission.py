def p(g,E=enumerate):
 for i,r in E(g):
  for j,v in E(r):
   if v>4:
    for x in g[i-1:i+2]:x[j-1:j+2]=1,1,1;r[j]=5
 return g
