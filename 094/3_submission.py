def p(g):
 for z in range(288):
  x,y=z//24,z%24//2
  if g[x][y]==g[x][y+1]==g[x+1][y]<2:g[x+2]=[c-2*(c>7) for c in g[x+2]]
  g=list(map(list,zip(*g)))
 return g