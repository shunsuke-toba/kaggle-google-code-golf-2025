p=lambda g:[[sum(r[c:c+3].count(6)for r in g[i:i+3])>1 for c in(0,4,8)]for i in(0,4,8)]
