def p(g):
 i,k=divmod(sum(g,[]).index(4),11);x=i&3;y=k&3;h=[[5*(r%4>2 or c%4>2)for c in range(11)]for r in range(11)]
 for t in 0,1,2:h[x*4+t][y*4:y*4+3]=g[i-x+t][k-y:k-y+3]
 return h