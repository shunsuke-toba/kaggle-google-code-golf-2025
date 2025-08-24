def p(g):k=max(z:=sum(g,[]),key=lambda x:z.index(x)+z[::-1].index(x));f=lambda a:[*zip(*filter(lambda r:k in r,a))];return f(f(g))
