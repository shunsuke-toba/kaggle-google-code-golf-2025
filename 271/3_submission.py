p=lambda g:max(([r[c:c+3]for r in g[i:i+3]]for i in range(len(g)-2)for c in range(len(g[0])-2)),key=lambda t:sum(r.count(1)*9+r.count(8)for r in t))
