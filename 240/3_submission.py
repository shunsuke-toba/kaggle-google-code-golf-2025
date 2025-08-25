def p(g):
 R=range(19)
 for i in R:
  for j in R:
   if v:=g[i][j]:g[j][~i]=g[~i][~j]=g[~j][i]=v
 for i in 1,3,5:
  for k in R[i+2:~i:2]:g[i][k]=g[~i][k]=g[k][i]=g[k][~i]=g[i][i+2]
 return g
