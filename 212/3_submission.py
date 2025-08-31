def p(g,b=100):
 while b:
  b-=1;v=g[r:=b//10][b%10];l=g.index([5]*10)
  while~r%11*(r-l)*v:g[r][b%10]=v;r+=(r<l)^(v<2)or-1
 return g