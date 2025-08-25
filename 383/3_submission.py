def p(g):f=sum(g,[]);a,b={*f}-{0};o=next(v for v in f if v);k=a+b-o;return[[(x:=c[0])+((0<r.count(o)<4)|(0<c[1:].count(o)<4))*(o-x-(o-k)*(x<1))for c in zip(r,*g)]for r in g]
