def p(g):t=g.index(next(filter(any,g)));l=len(g);return(g[t:t+3]*l)[-t%3:][:l]
