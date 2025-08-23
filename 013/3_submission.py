def p(g):
 (y,a),(Y,b)=[(j,v)for r in g for j,v in enumerate(r)if v];w=len(g[0])
 if{y,Y}<={0,w-1}:return[*map(list,zip(*p([*map(list,zip(*g))])))]
 if y>Y:y,Y,a,b=Y,y,b,a
 for r in g:d=Y-y;r[y::d]=([a,b]*9)[:(w-y+d-1)//d]
 return g
