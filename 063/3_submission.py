p=lambda g:[[x or 3*(max(t[j]for t in g[1:-1])*max(r[1:-1])<1)for j,x in enumerate(r)]for r in g]
