def p(g):
 t=2 in g[0]+g[-1]
 if t:g=[*map(list,zip(*g))]
 A=1-2*(2 in(r[-1]for r in g));B=1-2*(8 in g[-1])
 f=lambda g:[r[::A]for r in g[::B]];g=f(g);s=0
 for r in g[1:]:s+=r[0]>0;r[s:]=g[0][:-s or None]
 g=f(g);return[*map(list,zip(*g))]if t else g
