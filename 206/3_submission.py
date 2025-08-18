def p(g):
 W=len(g[0]);s,t=divmod(sum(g,[]).index(5),W)
 i,j=max((sum(v>0 for r in g[y:y+3]for v in r[x:x+3]),y,x)for y in range(len(g)-2)for x in range(W-2))[1:]
 for k in 0,1,2:g[s+k-1][t-1:t+2]=g[i+k][j:j+3]
 return g
