def p(g):
 for z in range(288):
  g=[*zip(*g)];x,y=z//24,z%24//2
  if 2>g[x][y]==g[x][y+1]==g[x+1][y]:g[x+2]=[c-c//8*2for c in g[x+2]]
 return g
