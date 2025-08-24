p=lambda g:(c:=[g[i][i]for i in range(len(g)//2)])and[[c[~c.index(x)]for x in r]for r in g]
