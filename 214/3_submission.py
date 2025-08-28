def p(g,r=0):
 for b in[0,1,2]*3:g[b][6-r]=g[~r][~b]=g[r][b];r+=b>1
 return g