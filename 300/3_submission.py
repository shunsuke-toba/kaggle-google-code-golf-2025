def p(g):f=lambda a,s=sum(g,[]):zip(*filter(lambda r:max({*s}-{0},key=s.count)in r,a));return(*f(f(g)),)
