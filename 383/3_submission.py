def p(g):o=next(filter(None,f:=sum(g,[])));return[[(x:=c[0])+((0<r.count(o)<4)|(0<c[1:].count(o)<4))*(o-x-(2*o-sum({*f}))*(x<1))for c in zip(r,*g)]for r in g]
