p=lambda g:(n:=sum(j<1 for i in g for j in i),(r:=range(3*n)))and[[(i//3*n+j//3<9-n)*g[i%3][j%3]for j in r]for i in r]
