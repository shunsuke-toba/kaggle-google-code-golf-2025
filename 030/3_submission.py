def p(g):t={};[t.setdefault(v,i)for i,r in enumerate(g)for v in r];n=[[0]*len(r)for r in g];[n[i+t[1]-t[v]].__setitem__(j,v)for i,r in enumerate(g)for j,v in enumerate(r)if v];return n
