def p(g):
 a,b={*sum(g,[])}-{0,8}
 for _ in[0]*280:g=[*zip(*[[c or(v==a)*b+a*(v==b)for c,v in zip(r,(0,*r))]for r in g[::-1]])]
 return g