def p(g):
 t=2in g[0]+g[-1];z=lambda g:[*map(list,zip(*g))]
 if t:g=z(g)
 a=2in z(g)[-1];b=8in g[-1];f=lambda g:[r[::1-2*a]for r in g[::1-2*b]]
 g=f(g);s=0
 for r in g[1:]:s+=r[0]>0;r[s:]=g[0][:-s or 99]
 return[z(f(g)),f(g)][1-t]
