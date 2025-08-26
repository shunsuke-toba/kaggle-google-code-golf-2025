p=lambda g,R=range(10):[[(c:=g[y][x],g[(y>4)*9][(x>4)*9])[c==3]for x in R]for y in R]
