def p(g):
 f=lambda x:[*map(list,zip(*x))]
 if T:=all(map(any,g)):g=f(g)
 for z in range(9**5):
  x,y=z//14%12+1,z%14
  if g[x][y]:g[x][y]=5
  else:g[x][y]=g[i:=x+1-2*(x<7)][y];g[i][y]=0
 return T and f(g)or g
