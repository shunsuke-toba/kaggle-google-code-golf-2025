p=lambda g:(w:=len(g[0]))>len(g)and[*zip(*p([*map(list,zip(*g))]))]or(r:=g.index([2]*w),h:=[r for r in g if 3in r],h[0]in g[:r]and p(g[::-1])[::-1]or(g[:r+1]+h+[[8]*w]+g[:1]*15)[:len(g)])[2]
