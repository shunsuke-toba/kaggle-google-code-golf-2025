def p(g):
 R=range(10);v=[[any(c[:i+1])*any(c[i:])*8for i in R]for c in zip(*g)]
 return[[v[j][i]|any(g[i][:j+1])*any(g[i][j:])*8for j in R]for i in R]