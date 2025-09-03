def p(g):
 for k in range(1700):g[i:=k%19][j:=k%18]|=g[i][j-2]*(9>i+3<j<i+8+(i<2))|g[j][i]|g[~i][j]
 return g