p=lambda g:(s:=sum(g,[]),c:=[i for i in s if s.count(i)==4][0])and[[c*(r[0]==r[-1]==c or g[0][j]==g[-1][j]==c)for j in range(len(r))]for r in g]
