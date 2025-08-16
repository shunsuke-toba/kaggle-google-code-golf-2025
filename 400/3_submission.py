p=lambda g:(lambda a,b:[[next(v for v in(g[i][~j],g[~i][j],g[~i][~j])if v-1)for j in range(b,b+5)]for i in range(a,a+5)])(*next((i,j)for i,r in enumerate(g)for j,c in enumerate(r)if c==1))
