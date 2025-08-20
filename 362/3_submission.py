def p(g):d=str(g).count('5');return[[c*(c!=5)for c in r[d:]+r[:d]]for r in g[-d:]+g[:-d]]
