def p(g):
 r=range(9);s={i for i in r if g[i//3][i%3]};T=str(g);n=0
 while 1:
  n+=1;y=n//8;x=n%8
  if{j for j in r if g[y+j//3][x+j%3]}==s and len(c:={g[y+j//3][x+j%3]for j in s})<2 and T.count(str(c:=c.pop()))==len(s):
   for j in s:g[y+j//3][x+j%3]=5
   return g
