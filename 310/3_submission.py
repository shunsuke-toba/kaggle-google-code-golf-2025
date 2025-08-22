def p(m):
 t=sum(m,[]);v=min({*t}-{0},key=t.count);f=lambda A:[i for i,a in enumerate(A)if v in a]
 L=f(m);C=f(zip(*m))
 return[r[C[0]:C[-1]+1]for r in m[L[0]:L[-1]+1]]
