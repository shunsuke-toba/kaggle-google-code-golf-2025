def p(j):
 a=[r.count(5)for r in zip(*j)]
 for r in j:
  for i in range(9):r[i]=[0,a[i]==max(a) or 2*(a[i]==min(filter(None,a)))][r[i]>4]
 return j
