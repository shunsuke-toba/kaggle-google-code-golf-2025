def p(g):
 (y,a),(Y,b)=sorted((r.index(v),v)for r in g for v in r if v);W=len(g[0])-1
 if Y%W<1:return[*zip(*p([*map(list,zip(*g))]))]
 Y-=y
 for r in g:r[y::Y]=([a,b]*8)[:(W-y)//Y+1]
 return g