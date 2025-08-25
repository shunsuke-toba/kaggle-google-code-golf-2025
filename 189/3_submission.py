p=lambda g,R=range(6):[r:=g[2][0]<8,c:=g[0][2]<8,[[g[i//3+r*7][j//3+c*7]*g[i+3-3*r][j+3-3*c]//3 for j in R]for i in R]][2]
