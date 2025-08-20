def p(g,A=range):
 r=[x[:]for x in g]
 for c in A(60):
  i,j=c//6,c%6
  F=g[i][j+2]
  if F>1:
   for y in A(i-2,min(i+3,9)):
    for x in A(j,j+5):
     if g[y][x]^1:r[y][x]=F
     if g[i-2][j]:r[i-3][x]=F
 return r