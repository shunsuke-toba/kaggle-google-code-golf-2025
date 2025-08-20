R=range(3);p=lambda g:[[sum(g[4*i+u][4*j+v]for u in R for v in R)>11 for j in R]for i in R]
