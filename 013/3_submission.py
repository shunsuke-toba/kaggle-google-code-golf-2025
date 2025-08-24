def p(g):
 (y,a),(Y,b)=sorted((j,v)for r in g for j,v in enumerate(r)if v);w=len(g[0])-1
 if{y,Y}<={0,w}:return[*map(list,zip(*p([*map(list,zip(*g))])))]
 for r in g:d=Y-y;r[y::d]=([a,b]*8)[:(w-y+d)//d]
 return g
