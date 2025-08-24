p=lambda g,R=range(11),r=range(3):[[max(g[i+x-1][j+y-1]for i in R for j in R if g[i][j]==5)for y in r]for x in r]

