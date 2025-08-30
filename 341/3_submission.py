def p(g):
 b=bytes(sum(g,[]));r,c=map(sorted,zip(*(divmod(F(k),10)for k in{*b}-{0}for F in(b.find,b.rfind))))
 x,y=r[1:3];c,d=c[1:3]
 for r in g[x+1:y]:r[c+1:d]=[8]*(d+~c)
 return g