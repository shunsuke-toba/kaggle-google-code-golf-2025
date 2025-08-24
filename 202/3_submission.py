p=lambda g,t=lambda a:[*zip(*a)]:len({*g[0]}-{0})>1 and t(p(t(g)))or[[0if any(s[i]<1 for s in g if max(s)==max(r))else v for i,v in enumerate(r)]for r in g]
