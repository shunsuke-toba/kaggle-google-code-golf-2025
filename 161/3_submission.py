p=lambda g:(c:=min(s:=sum(g,[]),key=s.count))and[[c*(r[0]==c or t[0]==c)for t in zip(*g)]for r in g]
