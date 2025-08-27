def p(g):
	a=6*g[3][5]//4
	for r in g[:3]:r[a:a+3]=r[5:2:-1]
	return g