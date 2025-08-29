def p(g):
 g=eval(str(g).replace('0','4'))
 for _ in [0]*96:g=[*zip(*[[c*(c^4+i*r[i-1]>0)for i,c in enumerate(r)]for r in g[::-1]])]
 return g