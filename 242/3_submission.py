def p(g):
 for b in range(196):
  r,c=b//14,b%14
  if g[r][c]==0:return[[g[15-r-i][15-c-j]for j in range(3)]for i in range(3)]