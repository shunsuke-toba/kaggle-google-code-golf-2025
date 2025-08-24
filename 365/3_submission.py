p=lambda g,R=range:max((all(F:=sum(S:=[t[x:X]for t in g[y:Y]],[])),F.count(2),len(F),S)for Y in R(11)for y in R(Y)for X in R(11)for x in R(X))[3]
