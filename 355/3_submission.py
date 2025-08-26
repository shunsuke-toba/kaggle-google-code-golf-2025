def p(g):s=sum(g,[]);return[[max({*s}-{c:=min(s,key=s.count)},key=lambda b:sum(r.count(c)for r in zip(*[q for q in g if b in q])if b in r))]]
