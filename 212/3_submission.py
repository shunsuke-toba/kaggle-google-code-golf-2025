def p(g):
 l=g.index([5]*10)
 for b in range(100):
  v=g[r:=b//10][c:=b%10]
  while v%5*(r-l)*~r*(10-r):g[r][c]=v;r+=(r<l)^(v<2)or-1
 return g
