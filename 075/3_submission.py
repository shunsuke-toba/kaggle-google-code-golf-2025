def p(g):
 for r in 1,4,7:
  for c in 5,8,11:
   if g[r][c]:
    for i in 0,1,2:g[r+i-1][c-1:c+2]=g[i][:3]
 return g
