def p(g,A=range):
 r=[*map(list,g)]
 for c in A(60):
  i,j=c//6,c%6;f=g[i][j+2]
  if f>1:
   for y in A(i-2,min(i+3,9)):
    for x in A(j,j+5):
     if g[i-2][j]:r[i-3][x]=f
     if g[y][x]^1:r[y][x]=f
 return r
