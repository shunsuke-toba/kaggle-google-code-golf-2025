def p(g):n=max(map(max,g));r=range(len(g));return[[1+i*j%n for j in r]for i in r]
