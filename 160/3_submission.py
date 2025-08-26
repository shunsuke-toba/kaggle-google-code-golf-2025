def p(g):
	for z in range(64):
		a,b,c=g[z>>3:][:3];z&=7;s=slice(z,z+3)
		if (a[s]+b[s]+c[s]).count(1)>7:a[s]=c[s]=0,2,0;b[s]=2,2,2
	return g