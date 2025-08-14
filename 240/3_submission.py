def p(g):
 n=19;c=[0]*10
 for j2 in range(n//2):
  for i in range(n):
   for j in[j2,n-j2-1]:
    if g[i][j]>0:
     c[g[i][j]]+=1
     if c[g[i][j]]==2:
      k=j2
      while k<=n-j2-1:g[i][k]=g[i][j];k+=2
 for _ in[1]*3:
  for i in range(n):
   for j in range(n):
    if g[i][j]>0:g[j][n-i-1]=g[i][j]
 return g