p=lambda g:(R:=range((n:=str(g).count('0'))*3))and[[g[i%3][j%3]*(i//3*n+j//3<9-n)for j in R]for i in R]
