def p(g):f=lambda s:[x for i,x in enumerate(s)if i<1 or s[i-1]^x];r=f(g[0]);return r[1:]and[r]or[[x]for x in f(next(zip(*g)))]
