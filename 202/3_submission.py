p=lambda g,t=lambda a:[*zip(*a)]:len({*g[0]}-{0})>1 and t(p(t(g)))or[[0if any(max(s)==max(r)>s[i]for s in g)else v for i,v in enumerate(r)]for r in g]
