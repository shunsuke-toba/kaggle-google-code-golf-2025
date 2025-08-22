def p(g):
 for z in range(81):
  i,j=z//9,z%9
  for x in (g[i][j]>4)*g[i-1:i+2]:x[j-1:j+2]=1,1,1;g[i][j]=5
 return g
