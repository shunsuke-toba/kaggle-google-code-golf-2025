def p(g):f=lambda m:[0]+[i for i,a in enumerate(m,1)if sum(a)<1]+[len(m)];C=f([*zip(*g)]);R=f(g);return[[next(v for r in g[a:b] for v in r[c:d] if v)for c,d in zip(C,C[1:])]for a,b in zip(R,R[1:])]
