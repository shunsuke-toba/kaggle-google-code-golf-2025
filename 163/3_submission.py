def p(g):
 i,k=divmod(sum(g,[]).index(4),11);h=[[5*(v==5)for v in r]for r in g]
 for t in 0,1,2:h[i%4*4|t][k%4*4:k%4*4|3]=g[i&-4|t][k&-4:][:3]
 return h
