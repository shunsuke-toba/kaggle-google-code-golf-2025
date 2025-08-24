p=lambda g,t=lambda a:[*map(list,zip(*a))]:len({*g[0]}-{0})>1 and t(p(t(g)))or([r.__setitem__(i,0)for r in g for s in g if max(s)==max(r)for i,x in enumerate(s)if x<1],g)[1]
