def p(g):
 e=g.index(max(g));k=g[0].index(max(g[0]))
 for i in-1,1:g[e+i][k-1:k+2]=4,4,4;g[e][k+i]=4
 return g