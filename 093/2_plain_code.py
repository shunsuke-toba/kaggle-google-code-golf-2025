f=lambda x:[*map(list,zip(*x))]
def p(g):
 if 5not in g[0]:return f(p(f(g)))
 for i in range(14):a1=g[i][:7].count(0);a2=g[i][7:].count(0);g[i]=[0]*a1+[5]*(14-a1-a2)+[0]*a2
 return g