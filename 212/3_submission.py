def p(g,b=100):
 while b:
  b-=1;l=g.index([5]*10);v=g[r:=b//10][b%10]
  while v%5*(r-l)*~r%11:g[r][b%10]=v;r+=(r<l)^(v<2)or-1
 return g