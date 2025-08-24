def p(g):d=g.count(g[0]);return[[c*(c!=5)for c in r[d:]+r[:d]]for r in g[-d:]+g[:-d]]
