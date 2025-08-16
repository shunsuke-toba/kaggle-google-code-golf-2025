p=lambda g:(r:=[{*a}-{0}for a in g],c:=[{*a}-{0}for a in zip(*g)],[[(s:=r[i]|c[j])and[2,sum(s)][len(s)<2]or 0 for j in range(len(c))]for i in range(len(r))])[2]
