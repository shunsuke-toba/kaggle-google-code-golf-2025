def p(g):e=enumerate;t={v:~i+len(g)for i,r in e(g[::-1])for v in r};n=[[0]*len(r)for r in g];[n[i+t[1]-t[v]].__setitem__(j,v)for i,r in e(g)for j,v in e(r)if v];return n
