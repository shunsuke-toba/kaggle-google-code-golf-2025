def p(g):
 a,*_,b=[i for i,c in enumerate(zip(*g))if 8 in c]
 for r in g:r[a:-~b]=[x+(8 in r and 2//x)for x in r[a:-~b]]
 return g
