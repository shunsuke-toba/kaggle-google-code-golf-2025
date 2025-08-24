def p(g):E=enumerate;a,b=zip(*((i,j)for i,r in E(g)for j,c in E(r)if c>1));return[[c*(c>1)for c in r[min(b):-~max(b)]]for r in g[min(a):-~max(a)]]
