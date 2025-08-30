def p(g):
 for y in range(64):a=y//8;y&=7;g[a+1][y+1]>>=g[a][y]*g[a+2][y+2]>0
 return g