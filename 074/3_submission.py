def p(g,A=range):
 E=[[g[r][c]if r<30and c<30else 9for c in A(32)]for r in A(32)]
 for _ in A(2):
  for r in A(32):
   for k in A(32):
    E[r][k]=min(E[r][k],E[31-r][k],E[k][r])
 return[E[r][:30]for r in A(30)]