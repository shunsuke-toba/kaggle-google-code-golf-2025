def p(g):
 e,k=[s.index(max(s))for s in(g,g[0])]
 for i in-1,1:g[e+i][k-1:k+2]=4,4,4;g[e][k+i]=4
 return g