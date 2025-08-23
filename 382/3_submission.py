def p(g):
 t=2in g[0]+g[-1];z=lambda g:[*map(list,zip(*g))]
 if t:g=z(g)
 a=1-2*(2in z(g)[-1]);b=1-2*(8in g[-1])
 f=lambda g:[r[::a]for r in g[::b]];g=f(g);s=0
 for r in g[1:]:s+=r[0]>0;r[s:]=g[0][:len(r)-s]
 return[f(g),z(f(g))][t]
