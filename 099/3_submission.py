def p(g,A=range):
 H=10;r=[x[:]for x in g]
 for i in A(H):
  for j in A(2,H-2):
   if g[i][j]>1:
    F=g[i][j]
    for ni in A(i-2,i+3):
     for nj in A(j-2,j+3):
      if ni<H and g[ni][nj]^1:r[ni][nj]=F
    if g[i-2][j-2]:
     for nj in A(j-2,j+3):
      if g[i-3][nj]^1:r[i-3][nj]=F
 return r