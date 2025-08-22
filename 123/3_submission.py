def p(g):r=range(10);c=[*filter(int,g[0])];return[[c[max(i,j)%len(c)]for j in r]for i in r]
