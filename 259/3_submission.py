def p(g):a,b=zip(*[(i,j)for i,r in enumerate(g)for j,c in enumerate(r)if c>1]);return[[c*(c>1)for c in r[min(b):-~max(b)]]for r in g[min(a):-~max(a)]]
