def p(g):
	s=sum(g,[]);m=min({*s}-{0},key=s.count)
	for _ in 0,1:g=[*zip(*[r for r in g if m in r])]
	return g