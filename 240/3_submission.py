def p(g):
 R=range(19)
 for i in R:
  for j in R:
   if v:=g[i][j]:g[j][~i]=g[~i][~j]=g[~j][i]=v
 for i in R[1:9:2]:
  if v:=g[i][i+2]:
   for k in R[i+2:~i:2]:g[i][k]=g[~i][k]=g[k][i]=g[k][~i]=v
 return g
