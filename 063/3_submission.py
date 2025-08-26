p=lambda g:[[x+3*(x<1)*(1-any(t[j]for t in g[1:-1])*any(r[1:-1]))for j,x in enumerate(r)]for r in g]
