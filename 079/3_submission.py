from collections import Counter as C
p=lambda g:[*map(list,k:=max(d:=C(tuple(map(tuple,s))for i in range(len(g)-2)for j in range(len(g[0])-2)for s in[[r[j:j+3]for r in g[i:i+3]]]if sum(c>0 for r in s for c in r)>2 and all(map(sum,s))and all(map(sum,zip(*s)))),key=lambda k:(d[k],sum(c>0 for r in k for c in r))))]
