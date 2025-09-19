def p(g):
 for r in g[2:]:r[:]=[max(r)]*6;r[g[0].index(8)]=8-r[0]*2
 return g