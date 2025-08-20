p=lambda g:[[r[j]or r[j+5]or s[j]or s[j+5]for j in range(4)]for r,s in zip(g,g[5:])]
