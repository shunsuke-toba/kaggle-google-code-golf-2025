p=lambda g,R=range(6):(r:=g.index(9*[8]),c:=g[0].index(8),[[g[r//6*7+i//3][c//6*7+j//3]*g[3*(r<4)+i][3*(c<4)+j]//3 for j in R]for i in R])[-1]
