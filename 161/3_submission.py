p=lambda g:(s:=sum(g,[]),c:=s[[*map(s.count,s)].index(4)])and[[c*(r[0]==r[-1]==c or x==y==c)for x,y in zip(g[0],g[-1])]for r in g]
