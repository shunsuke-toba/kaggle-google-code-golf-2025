p=lambda g:(R:=range(d:=str(g).count('0')*3))and[[g[i%3][j%3]*(i//3*d+j<27-d)for j in R]for i in R]
