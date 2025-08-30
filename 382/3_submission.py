def p(g):
 *t,=map(list,zip(*g))
 if 2in g[0]+g[-1]:return[*zip(*p(t))]
 a,b=2in t[-1],8in g[-1];f=lambda:[r[::1-2*a]for r in g[::1-2*b]];g=f();s=0
 for r in g:s+=r[0]>0;r[s:]=g[0][:-s or 99]
 return f()