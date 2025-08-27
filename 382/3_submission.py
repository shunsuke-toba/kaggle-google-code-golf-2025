def p(g):
 z=lambda:[*map(list,zip(*g))];s=0
 if t:=2in g[0]+g[-1]:g=z()
 a=2in z()[-1];b=8in g[-1];f=lambda g:[r[::1-2*a]for r in g[::1-2*b]];g=f(g)
 for r in g:s+=r[0]>0;r[s:]=g[0][:-s or 99]
 return(g:=f(g),z())[t]