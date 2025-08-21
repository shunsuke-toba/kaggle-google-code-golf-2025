def p(g,e=enumerate):
	y=[i for i,r in e(g)if 8 in r];x=[i for i,c in e(zip(*g))if 8 in c]
	for i in y:
		for j in range(x[0],-~x[-1]):g[i][j]+=2*(g[i][j]==1)
	return g
