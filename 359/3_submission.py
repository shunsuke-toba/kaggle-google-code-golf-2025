p=lambda g:[[max((v:=r+[q[j]for q in g]),key=v.count)for j in range(len(r))]for r in g]

