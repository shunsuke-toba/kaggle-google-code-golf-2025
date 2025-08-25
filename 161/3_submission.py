p=lambda g:(c:=min(s:=sum(g,[]),key=s.count))and[[c*(r[0]==r[-1]==c or t[0]==t[-1]==c)for t in zip(*g)]for r in g]
