def p(g):
 m,n=map(min,zip(*[(k//10,k%10)for k,v in enumerate(sum(g,[]))if v]))
 r=range(5)
 for i in r:g[m+i][n:n+5]=[max(g[m+i][n+j],g[m+4-j][n+i],g[m+4-i][n+4-j],g[m+j][n+4-i])for j in r]
 return g
