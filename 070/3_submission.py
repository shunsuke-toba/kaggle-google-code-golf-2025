def p(g):
 a,*_,b=[i for i,c in enumerate(zip(*g))if 8in c]
 for r in g:r[a:-~b]=[x|x%2*2*(8in r)for x in r[a:-~b]]
 return g