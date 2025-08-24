def p(g):
 s=[i for i in range(9)if g[i//3][i%3]];a=s[0]
 for n in range(1,64):
  y,x=divmod(n,8)
  if{g[y+i//3][x+i%3]for i in s}=={c:=g[y+a//3][x+a%3]}and str(g).count(str(c))==len(s):
   for i in s:g[y+i//3][x+i%3]=5
   return g
