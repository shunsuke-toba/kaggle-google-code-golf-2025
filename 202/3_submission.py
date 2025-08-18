p=lambda g,t=lambda a:[*map(list,zip(*a))]:t(p(t(g)))if any({*r}-{0,max(r)}for r in g)else([r.__setitem__(i,0)for r in g for s in g if max(s)==max(r)for i,x in enumerate(s)if x<1],g)[1]
