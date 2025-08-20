def p(g):g=g[0];c=g.index(0);return[g[:1]*i+g[i:]for i in range(c,c+len(g)//2)]
