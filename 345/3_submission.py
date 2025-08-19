def p(g):
 for x in range(10):
  if g[9][x]:
   y=9
   while y:k=g[y-1][x]==5;g[y-1+k][x+k]=2;y-=1-k;x+=k
 return g