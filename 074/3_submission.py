def p(g):
 for k in range(9999):i=k%30;j=k%31%30;g[i][j]=g[j][i]%9|g[i][1-j]*(j>1)%9|g[i][j]%9
 return g