def p(g):
 for b in range(9):r=b//3;b%=3;g[b][6-r]=g[~r][~b]=g[r][b]
 return g