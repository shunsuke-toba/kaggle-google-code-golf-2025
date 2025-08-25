def p(g):f=lambda a,s=sum(g,[]):zip(*[r for r in a if max({*s}-{0},key=s.count)in r]);return(*f(f(g)),)
