def p(g):
 t=[*zip(*g)]
 if 2in g[0]+g[-1]:return[*zip(*p(t))]
 b=8in g[-1];f=lambda:[[*r][::1-2*(2in t[-1])]for r in g[::1-2*b]];s=0
 for r in(g:=f()):s+=r[0]>0;r[s:]=g[0][:-s or 99]
 return f()