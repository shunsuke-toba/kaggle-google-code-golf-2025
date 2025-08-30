def p(g):
 m=[*map(any,g)].index(1);n=[*map(any,zip(*g))].index(1)
 for k in range(75):i=k//5%5;g[m+i][n+k%5]|=g[m+~k%5][n+i]
 return g