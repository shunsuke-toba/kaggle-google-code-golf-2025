def p(g):
 for k in range(950):g[i:=k%19][j:=k%18]|=g[i][j-2]*(i<j-3<7)|g[j][i]|g[j][~i]
 return g