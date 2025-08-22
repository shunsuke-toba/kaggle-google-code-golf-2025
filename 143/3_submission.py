def p(g):
 r=range(9);s={i for i in r if g[i//3][i%3]};T=str(g)
 for n in range(1,64):
  y,x=divmod(n,8)
  if {i for i in r if g[y+i//3][x+i%3]}==s:
   c={g[y+i//3][x+i%3]for i in s}
   if len(c)<2 and T.count(str(c:=c.pop()))==len(s):
    for i in s:g[y+i//3][x+i%3]=5
    return g
