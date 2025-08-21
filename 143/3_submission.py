def p(g):
 s={k for k in range(9) if g[k//3][k%3]};t=next(iter(s));S=str(g)
 for n in range(1,64):
  y=n//8;x=n%8
  if {k for k in range(9) if g[y+k//3][x+k%3]}==s:
   C={g[y+k//3][x+k%3]for k in s}
   if len(C)==1 and S.count(str(c:=C.pop()))==len(s):
    for k in s:g[y+k//3][x+k%3]=5
    return g
 return g
