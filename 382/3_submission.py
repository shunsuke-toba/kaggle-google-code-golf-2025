def p(g):
 t=2 in g[0]+g[-1]
 if t:g=[*map(list,zip(*g))]
 a=1-2*(2 in[*zip(*g)][-1]);b=1-2*(8 in g[-1])
 f=lambda g:[r[::a]for r in g[::b]];g=f(g);s=0
 for r in g[1:]:s+=r[0]>0;r[s:]=g[0][:len(r)-s]
 return t and[*map(list,zip(*f(g)))]or f(g)
