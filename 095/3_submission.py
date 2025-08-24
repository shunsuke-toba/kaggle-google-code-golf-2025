def p(g):
 for z in range(81):
  i=z//9;z%=9
  for x in(g[i][z]>4)*g[i-1:i+2]:x[z-1:z+2]=1,1,1;g[i][z]=5
 return g
