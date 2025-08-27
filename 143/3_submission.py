def p(g):
 s=[i for i in range(9)if g[i//3][i%3]];n=1
 while len(c:={g[n//8+i//3][n%8+i%3]for i in s})-1 or sum(g,[]).count(c.pop())-len(s):n+=1
 for i in s:g[n//8+i//3][n%8+i%3]=5
 return g