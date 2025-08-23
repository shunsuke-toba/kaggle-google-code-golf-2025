def p(g):
 a,b={*sum(g,[])}-{0};o=(b,a)[any({*r}-{0}=={a}for r in g)];k=a+b-o
 return[[(x:=c[0])+((0<r.count(o)<4)|(0<c[1:].count(o)<4))*((x<1)*k+(x==k)*(o-x))for c in zip(r,*g)]for r in g]