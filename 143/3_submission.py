def p(g):
 s=[i for i in range(9)if g[i//3][i%3]]
 for n in range(1,64):
  if len(c:={g[n//8+i//3][n%8+i%3]for i in s})<2 and sum(g,[]).count(c.pop())==len(s):
   for i in s:g[n//8+i//3][n%8+i%3]=5
   return g