def p(g):
 s=sum({*sum(g,[])})-8
 for _ in[0]*280:g=[*zip(*[[c or v%8and s-v for c,v in zip(r,(0,*r))]for r in g[::-1]])]
 return g