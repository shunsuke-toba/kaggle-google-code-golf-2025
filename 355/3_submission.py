def p(g):return[[max(s:=sum(g,[]),key=lambda b:sum(r.count(m:=min(s,key=s.count))for r in zip(*[q for q in g if b in q])if b in r)*(b!=m))]]
