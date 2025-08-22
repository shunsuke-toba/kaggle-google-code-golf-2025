p=lambda g:[[max(range(1,10),key=lambda c:max(r.count(c)for r in g)*sum(c in r for r in g))]*2]*2
