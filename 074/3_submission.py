def p(g,A=range):
 E=[[g[r][c]if r<30and c<30else 9for c in A(32)]for r in A(32)]
 for _ in A(2):
  for r in A(32):
   for c in A(32):E[r][c]=min(E[r][c],E[31-r][c],E[c][r])
 return[E[r][:30]for r in A(30)]