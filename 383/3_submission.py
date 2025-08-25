def p(g):f=sum(g,[]);o=next(filter(None,f));return[[(x:=c[0])+((0<r.count(o)<4)|(0<c[1:].count(o)<4))*(o-x-(o-(sum({*f}-{0})-o))*(x<1))for c in zip(r,*g)]for r in g]
