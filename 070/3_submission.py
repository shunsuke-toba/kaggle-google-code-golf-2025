def p(g):
 c=[8in k for k in zip(*g)]
 a=c.index(1);b=a+sum(c)
 for r in g:r[a:b]=[x|2&-x*(8in r)for x in r[a:b]]
 return g