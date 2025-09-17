def p(g):
 for a in range(-2,8):
  for b in range(-2,8):
   for c in range(-2,8):
    for d in range(-2,8):
     if all(g[a+i][b+j]^g[c+i][d+j]for i in range(3)for j in range(3)):
      return[[g[a+i][b+j]^g[c+i][d+j]for j in range(3)]for i in range(3)]