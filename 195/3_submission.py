p=lambda g,A=range(9):(r:=min(i for i,R in enumerate(g)if 5 in R),c:=min(R.index(5)for R in g if 5 in R),[[g[r+x//3*3][c+y//3*3]and g[r+x%3*3][c+y%3*3]for y in A]for x in A])[2]
