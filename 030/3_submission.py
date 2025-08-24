def p(g):e=enumerate;t={v:i for i,r in e(g)for v in r};n=[[0]*10for _ in g];[n[i+t[1]-t[v]].__setitem__(j,v)for i,r in e(g)for j,v in e(r)if v];return n
