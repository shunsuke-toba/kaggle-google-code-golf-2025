p=lambda g,r=range(8):[[(j%5>2>1<(a:=g[i][j-3])==g[i][j+3]or i%5>2>1<(a:=g[i-3][j])==g[i+3][j])and a or g[i][j]for j in r]for i in r]
