def p(g):
 e,k=[s.index(max(s))for s in(g,g[0])]
 for t in b'01235678':g[e+t//3-17][k+t%3-1]=4
 return g