def p(g):
 if g[12:]:return[*zip(*p([*map(list,zip(*g))]))]
 (y,a),(Y,b)=sorted((r.index(v),v)for r in g for v in r if v)
 for r in g:r[y::Y-y]=([a,b]*8)[:len(r[y::Y-y])]
 return g