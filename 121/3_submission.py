def p(g):f=sum(g,[]);i=f.index(8);g=[f[i+c:i+c+3]for c in(-14,-1,12)];g[1][1]=max({*sum(g,[])}-{8});return g
