def p(g):
 i,k=divmod(sum(g,[]).index(4),11);x=i&3;y=k&3;h=[[5*(v==5)for v in r]for r in g]
 for t in 0,1,2:h[x*4+t][y*4:y*4+3]=g[i-x+t][k-y:][:3]
 return h
