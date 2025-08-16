def p(g,m=max):e,a=m(map(m,g[:5])),m(map(m,g[5:]));return[[(e,a)[r>4]*(r%7in(0,2)or c%9<1)for c in range(10)]for r in range(10)]
