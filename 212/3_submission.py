def p(g,b=99):
 if b:p(g,b-1)
 v=g[r:=b//10][b%10];l=g.index([5]*10)
 while~r%11*(r-l)*v:g[r][b%10]=v;r+=v%2^(r<l)or-1
 return g