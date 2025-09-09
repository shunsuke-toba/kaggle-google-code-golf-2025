def p(g,i=-1):
 while 0in g[0]:g=g[1:]
 if i>2:g=[[(c,r[0])[r[0]in r[j:]]for j,c in enumerate(r)]for r in g]
 return p([*zip(*g)][::-1],i+1)if i<7 else g