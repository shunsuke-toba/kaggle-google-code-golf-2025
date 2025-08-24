p=lambda g:(s:=sum(g,[]),c:=s[[*map(s.count,s)].index(4)])and[[c*(r[0]==r[-1]==c or t[0]==t[-1]==c)for t in zip(*g)]for r in g]
