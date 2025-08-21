p=lambda g,R=range(17):[g[r][c]<g[r%6][c%6]and g[r].__setitem__(c,g[5][5])for r in R for c in R]and g
