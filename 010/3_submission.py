def p(a):
	b={}
	for r in a:
		for i in range(9):
			if r[i]:r[i]=b.setdefault(i,-~len(b))
	return a
