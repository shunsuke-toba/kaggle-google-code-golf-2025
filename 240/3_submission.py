R=range(19)
def p(g):
 for r in R:
  for c in R:g[r][c]|=g[r][~c]|g[~r][c]|g[~r][~c]
 for i in 1,3,5:
  for k in R[i+2:~i:2]:g[i][k]=g[~i][k]=g[k][i]=g[k][~i]=g[i][i+2]
 return g