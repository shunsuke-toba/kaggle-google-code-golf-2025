def p(g):
 m=[*map(any,g)].index(1);n=[*map(any,zip(*g))].index(1)
 for k in range(25):j=k%5;i=k//5;g[m+i][n+j]|=g[m+4-j][n+i]|g[m+4-i][n+4-j]|g[m+j][n+4-i]
 return g