p=lambda g,R=range(17):[[g[r][c]or g[r%6][c%6]and g[5][5]for c in R]for r in R]
