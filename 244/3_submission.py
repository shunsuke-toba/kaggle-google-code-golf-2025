def p(g):
 n=len(g[0])
 for p in range(n):
  if g[0][p]!=g[0][p+1]:A=range(0,n,p+2);return[[g[i][j]for j in A][::-1]for i in A]