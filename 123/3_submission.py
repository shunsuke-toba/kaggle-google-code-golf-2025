def p(g):c=[*filter(None,g[0])];r=range(10);return[[c[max(i,j)%len(c)]for j in r]for i in r]
