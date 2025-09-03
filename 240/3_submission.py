def p(g):
 for k in range(1700):g[i:=k%19][j:=k%18]|=g[i][j-2]*(i+3<j<10)|g[j][i]|g[~i][j]
 return g