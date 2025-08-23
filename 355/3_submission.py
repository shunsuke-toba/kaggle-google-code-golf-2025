f=lambda a,b:zip(*filter(lambda r:b in r,a))
def p(g):s=sum(g,[]);return[[max({*s}-{c:=min(s,key=s.count)},key=lambda b:sum(r.count(c)for r in f(f(g,b),b)))]]