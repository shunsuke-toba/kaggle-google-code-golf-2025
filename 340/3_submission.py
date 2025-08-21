def p(g):
 z=[*zip(*g)]
 for r in g[1:-1]:a=r[1:-1];r[1:-1]=[0]*len(a);r[1]=r[0]*(r[0]in a);r[-2]=r[-1]*(r[-1]in a)
 for j,c in enumerate(z[1:-1],1):g[1][j]=(c[0]in c[1:])*c[0];g[-2][j]=(c[-1]in c[:-1])*c[-1]
 return g
