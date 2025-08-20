def p(g):e,k=[[*map(all,t)].index(1) for t in (g,zip(*g))];g[e-1][k-1:k+2]=g[e+1][k-1:k+2]=[4]*3;g[e][k-1]=g[e][k+1]=4;return g
