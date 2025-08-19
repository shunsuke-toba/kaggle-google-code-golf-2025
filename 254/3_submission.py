def p(j):a=[r.count(5)for r in zip(*j)];return[[r[i]>4and(a[i]==max(a)or(a[i]==min({*a}-{0}))*2)for i in range(9)]for r in j]
