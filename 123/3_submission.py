def p(g):c=[*filter(None,g[0])];m=len(c);return[[c[max(i,j)%m]for j in range(10)]for i in range(10)]
