def p(g):
 for k in range(2200):g[i][j]=min(g[j:=k%31%30][i:=k%30],g[i][j^(j>1)*31])
 return g