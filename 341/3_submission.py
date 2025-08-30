def p(g):
 b=bytes(sum(g,[]));r,c=map(sorted,zip(*(divmod(F(k),10)for k in{*b}-{0}for F in(b.find,b.rfind))))
 for r in g[r[1]+1:r[2]]:r[c[1]+1:c[2]]=[8]*(c[2]+~c[1])
 return g