def p(g):
 s=[i for i in range(9)if g[i//3][i%3]];n=1
 while{(v:=g[n//8+i//3][n%8+i%3])for i in s}-{v}or len(s)<sum(g,[]).count(v):n+=1
 for i in s:g[n//8+i//3][n%8+i%3]=5
 return g