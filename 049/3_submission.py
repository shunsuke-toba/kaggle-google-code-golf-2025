p=lambda g:(s:=sum(g,[]),c:=min({*s}-{0},key=s.count),w:=max(r.count(c)for r in g),[[c]*w]*(s.count(c)//w))[3]
