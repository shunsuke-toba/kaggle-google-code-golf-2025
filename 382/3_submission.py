def p(g):
 *t,=zip(*g);b=g[-1];f=lambda:[[*r][::2in t[0]or-1]for r in g[::1-2*(8in b)]];s=0
 if 2in g[0]+b:return[*zip(*p(t))]
 for r in(g:=f()):s+=r[0]>0;r[s:]=g[0][:-s or 99]
 return f()