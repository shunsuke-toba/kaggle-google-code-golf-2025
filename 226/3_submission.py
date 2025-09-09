def p(g):
 g[0][0]=1;g[9][9]=3;g[4|g[4][0]][4|g[0][4]]=2
 for _ in g*2:*g,=zip(*[[b|(5>a>b)*a for a,b in zip([5,*r],r)]for r in g][::-1])
 return g