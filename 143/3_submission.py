def p(g):
 s=[i for i in range(9)if g[i//3][i%3]]
 for n in range(1,64):
  y=n//8;x=n%8
  if(c:={g[y+i//3][x+i%3]for i in s})and len(c)<2 and str(g).count(str(c.pop()))==len(s):
   for i in s:g[y+i//3][x+i%3]=5
   return g
