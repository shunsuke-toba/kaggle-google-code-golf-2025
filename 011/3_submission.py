def p(g):
 for I in 0,4,8:
  for J in 0,4,8:
   b=[r[J:J+3]for r in g[I:I+3]]
   if 8 in sum(b,[]):continue
   return [[5 if i%4==3 or j%4==3 else b[i//4][j//4]for j in range(11)]for i in range(11)]
