def p(g):
	f=sum(g,[]);w=len(g[0])
	for v in {*f}-{0}:
		i=f.index(v);j=f.index(v,-~i);c,d=sorted((i%w,j%w))
		for R in g[i//w:j//w+1]:R[c:d+1]=[v]*-~(d-c)
	return g