def p(g):
 s=[i for i in range(9)if g[i//3][i%3]]
 for n in range(1,64):
  if 2>len(c:={g[n//8+i//3][n%8+i%3]for i in s})<=len(s)==sum(g,[]).count(c.pop()):
   for i in s:g[n//8+i//3][n%8+i%3]=5
   return g

