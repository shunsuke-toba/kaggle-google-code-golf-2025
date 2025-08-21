def p(g):
 for r in 1,4,7:
  for c in 5,8,11:
   for i in range(g[r][c]*3):g[r+i-1][c-1:c+2]=g[i][:3]
 return g
