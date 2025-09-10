def p(g):
 for s in[sum({*sum(g,[])})-8]*280:*g,=zip(*(map(lambda c,v:c or v%8and s-v,r,(0,*r))for r in g[::-1]))
 return g