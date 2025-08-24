p=lambda g,d={}.fromkeys:(x:=[*d(g[0])],x[1:]and[x]or[*zip(d(next(zip(*g))))])[1]
