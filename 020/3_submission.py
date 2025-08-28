def p(g):
 m=[*map(any,g)].index(1);n=[*map(any,zip(*g))].index(1)
 for _ in'123':
  for k in range(25):j=k%5;i=k//5;g[m+i][n+j]|=g[m+4-j][n+i]
 return g