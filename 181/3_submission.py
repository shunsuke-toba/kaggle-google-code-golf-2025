def p(g):
	a=g[3][3]<1
	for r in g[:3]:r[a*6:a*6+3]=r[3:6][::-1]
	return g
