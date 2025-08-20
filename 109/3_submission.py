def p(g):
 n=len(g)//2;g=[r+r[::-1]for r in[[e and g[0][n]for e in r[:n]]for r in g[:n]]];return g+g[::-1]
