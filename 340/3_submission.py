def p(g):
 Z=[*zip(*g)];T=[r[1:-1]for r in g[1:-1]]
 for r in g[1:-1]:r[1:-1]=[0]*(len(Z)-2)
 for j,c in enumerate(Z[1:-1],1):g[1][j]=(c[0]in c[1:])*c[0];g[-2][j]=(c[-1]in c[:-1])*c[-1]
 for r,q in zip(g[1:-1],T):r[1]=(r[0]in q)*r[0];r[-2]=(r[-1]in q)*r[-1]
 return g