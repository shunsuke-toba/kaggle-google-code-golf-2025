def p(g):
 for r in 1,4,7:
  for c in 5,8,11:
   for i in(-1,0,1)*g[r][c]:g[r+i][c-1:c+2]=g[i+1][:3]
 return g