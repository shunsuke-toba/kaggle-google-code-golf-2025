f=lambda a,b:zip(*[r for r in a if b in r])
def p(g):s=sum(g,[]);return[[max({*s}-{c:=min(s,key=s.count)},key=lambda b:sum(f(f(g,b),b),()).count(c))]]