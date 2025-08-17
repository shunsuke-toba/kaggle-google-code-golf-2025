def p(g):
 r=range
 for i in r(1,len(g),4):
  for j in r(1,len(g[0]),4):
   v=g[i][j]+5
   for a in g[i-1:i+2]:a[j-1:j+2]=[v]*3
 return g
