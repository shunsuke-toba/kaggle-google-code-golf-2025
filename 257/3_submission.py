p=lambda g,A=range(4):[[g[i][j]or g[i][j+5]or g[i+5][j]or g[i+5][j+5]for j in A]for i in A]
