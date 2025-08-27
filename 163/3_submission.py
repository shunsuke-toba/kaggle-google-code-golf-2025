def p(g):
 i,k=divmod(sum(g,[]).index(4),11);h=[[5*(v==5)for v in r]for r in g];b=k%4*4
 for t in 0,1,2:h[i%4*4|t][b:b|3]=g[i&-4|t][k&-4:k|3]
 return h